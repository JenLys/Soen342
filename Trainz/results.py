import recordDB
from connection import Connection

class Journey:
    def __init__(self, connections):
        # connections: list[Connection] (one or more)
        self.connections = connections

    def calculatePrice(self, first_class=False):
        """Return total price (by default 2nd class)."""
        return sum((c.fclass_rate if first_class else c.sclass_rate) for c in self.connections)

    def _parse_time_minutes(self, tstr):
        """Parse 'HH:MM' into minutes since midnight. Returns int."""
        if tstr.find(" (+1d)"):
            tstr = tstr.replace(" (+1d)", "")
        try:
            parts = tstr.strip().split(':')
            h = int(parts[0]) % 24
            m = int(parts[1])
            return h * 60 + m
        except Exception:
            return 0

    def totalDuration(self):
        """Sum durations of the whole journey in minutes."""
        duration = 0

        for connection in self.connections:
            if connection.arr_time.find("(+1d)") != -1:
                duration = duration + (24 * 60 - self._parse_time_minutes(connection.dep_time)) + self._parse_time_minutes(connection.arr_time)
            else:
                duration = duration + self._parse_time_minutes(connection.arr_time) - self._parse_time_minutes(connection.dep_time)

        duration = duration + self._parse_time_minutes(self.calcLayoverTime())
        return duration
    
    def calcLayoverTime(self):
        layoverTime = 0
        dep_time = 0
        arr_time = self._parse_time_minutes(self.connections[0].dep_time)

        for connection in self.connections:
            dep_time = self._parse_time_minutes(connection.dep_time)
            layoverTime = layoverTime + dep_time - arr_time
            arr_time = self._parse_time_minutes(connection.arr_time)

        layoverTime = f"{layoverTime // 60}:{layoverTime % 60}"

        return layoverTime

    def stops(self):
        return len(self.connections) - 1
    
    def showDaysOfOp(self):
        str = ""
        for key in self.days:
            if self.days[key]:
                str += key + ", "

        str = str.removesuffix(", ")
        return str

    def __str__(self):
        path = " → ".join([c.dep_city for c in self.connections] + [self.connections[-1].arr_city])
        price = self.calculatePrice(first_class=False)
        hours = self.totalDuration() // 60
        mins = self.totalDuration() % 60
        return f"{path} | {len(self.connections)} connection(s) | tot duration {hours}h{mins}m | layover time {self.calcLayoverTime()} | dep time: {self.connections[0].dep_time} | arr time : {self.connections[len(self.connections) - 1].arr_time} | days of op: {self.showDaysOfOp()} | €{price:.2f}"
    
def commonDaysOfOp(days1, days2):
    commonDays ={"Mon": False, 
                "Tue": False, 
                "Wed": False, 
                "Thu": False, 
                "Fri": False, 
                "Sat": False,
                "Sun": False}
    for key in commonDays:
        if days1[key] and days2[key]:
            commonDays[key] = True

    return commonDays

def validateJourney2(journey: Journey):
    arr_time = 0
    dep_time = 0
    extra_days_count = 0

    keys = list(journey.connections[0].days.keys())

    commonDays = journey.connections[0].days

    for connection in journey.connections:
        commonDays = commonDaysOfOp(commonDays, connection.days)

        has_overlap = False
        for key in commonDays:
            if commonDays[key]:
                has_overlap = True
                break
        
        if not has_overlap:
            return False
        
        if connection.arr_time.find("(+1d)") != -1:
            extra_days_count = extra_days_count + 1
            new_days = {"Mon": False, 
                        "Tue": False, 
                        "Wed": False, 
                        "Thu": False, 
                        "Fri": False, 
                        "Sat": False,
                        "Sun": False}
            
            for index in range(0, 7):
                if commonDays[keys[index]]:
                    new_days[keys[(index + 1) % 7]] = True
            commonDays = new_days

    for connection in journey.connections:
        dep_time = journey._parse_time_minutes(connection.dep_time)
        if not arr_time <= dep_time:
            return False
        arr_time = journey._parse_time_minutes(connection.arr_time)

    for index in range(0, extra_days_count):
        new_days = {"Mon": False, 
                    "Tue": False, 
                    "Wed": False, 
                    "Thu": False, 
                    "Fri": False, 
                    "Sat": False,
                    "Sun": False}
        for index in range(0, 7):
            if commonDays[keys[index]]:
                new_days[keys[(index - 1) % 7]] = True
        commonDays = new_days

    journey.days = commonDays
        
    return True

def validateJourney(journey: Journey):
    arr_time = 0
    dep_time = 0

    for connection in journey.connections:
        if connection.arr_time.find("(+1d)") != -1:
            return validateJourney2(journey)

    for connection in journey.connections:
        dep_time = journey._parse_time_minutes(connection.dep_time)
        if not arr_time <= dep_time:
            return False
        arr_time = journey._parse_time_minutes(connection.arr_time)

    commonDays = journey.connections[0].days
    for connection in journey.connections:
        commonDays = commonDaysOfOp(commonDays, connection.days)

    for key in commonDays:
        if commonDays[key]:
            journey.days = commonDays
            return True

    return False

def searchForConnections(db, dep_station, arr_station, max_depth=2):
    """
    Find all journeys from dep_station to arr_station (up to max_depth connections).
    Returns list[journey].
    """
    journeys = []

    def dfs(current_city, target_city, path, depth):
        if depth > max_depth:
            return
        # iterate over connections starting from current_city
        for con in db.getConnectionsFrom(current_city):
            # avoid immediate cycle: don't reuse the same connection object,
            # and avoid visiting same city twice in path to prevent cycles
            if any(c is con for c in path):
                continue
            if any(c.dep_city == con.arr_city for c in path):
                # we already visited this city as departure -> avoid cycle
                continue

            new_path = path + [con]
            if con.arr_city == target_city:
                journey = Journey(new_path)
                if validateJourney(journey):
                    journeys.append(journey)
            else:
                dfs(con.arr_city, target_city, new_path, depth + 1)

    dfs(dep_station, arr_station, [], 1)
    return journeys

def sortByDuration(journeys, ascending=True):
    return sorted(journeys, key=lambda t: t.totalDuration(), reverse=not ascending)

def sortByPrice(journeys, ascending=True, first_class=False):
    return sorted(journeys, key=lambda t: t.calculatePrice(first_class=first_class), reverse=not ascending)

def printJourneys(journeys, limit=None):
    """Nicely print journeys; returns nothing. limit=None prints all."""
    if not journeys:
        print("No journeys found.")
        return
    if limit:
        journeys = journeys[:limit]
    for i, t in enumerate(journeys, start=1):
        print(f"{i}. {t}")

# every train of the journey must be trainType for this to return something
def filterByTrainType(trainType, journeys):
    filteredList = []
    for journey in journeys:
        for connection in journey.connections:
            if connection.train_type == trainType:
                filteredList.append(journey)
                
    return filteredList

# every corresponding dayOfWeek of the journey must be true for this to return something
def filterByDayOfWeek(dayOfWeek, journeys):
    filteredList = []
    for journey in journeys:
        for connection in journey.connections:
            if connection.days[dayOfWeek] == True:
                filteredList.append(journey)

    return filteredList
