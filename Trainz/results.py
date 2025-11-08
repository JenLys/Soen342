import recordDB
from connection import Connection

class Trip:
    def __init__(self, connections):
        # connections: list[Connection] (one or more)
        self.connections = connections

    def calculatePrice(self, first_class=False):
        """Return total price (by default 2nd class)."""
        return sum((c.fclass_rate if first_class else c.sclass_rate) for c in self.connections)

    def _parse_time_minutes(self, tstr):
        """Parse 'HH:MM' into minutes since midnight. Returns int."""
        try:
            parts = tstr.strip().split(':')
            h = int(parts[0]) % 24
            m = int(parts[1])
            return h * 60 + m
        except Exception:
            return 0

    def totalDuration(self):
        """Sum durations of the whole trip in minutes."""
        dep_time = self._parse_time_minutes(self.connections[0].dep_time)
        arr_time = self._parse_time_minutes(self.connections[len(self.connections) - 1].arr_time)
        total = arr_time - dep_time
        return total
    
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

        return str

    def __str__(self):
        path = " >> ".join([c.dep_city for c in self.connections] + [self.connections[-1].arr_city])
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

def validateTrip(trip: Trip):
    arr_time = 0
    dep_time = 0

    for connection in trip.connections:
        dep_time = trip._parse_time_minutes(connection.dep_time)
        if not arr_time <= dep_time:
            return False
        arr_time = trip._parse_time_minutes(connection.arr_time)

    commonDays = trip.connections[0].days
    for connection in trip.connections:
        commonDays = commonDaysOfOp(commonDays, connection.days)

    for key in commonDays:
        if commonDays[key]:
            trip.days = commonDays
            return True

    return False

def searchForConnections(db, dep_station, arr_station, max_depth=2):
    """
    Find all trips from dep_station to arr_station (up to max_depth connections).
    Returns list[Trip].
    """
    trips = []

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
                trip = Trip(new_path)
                if validateTrip(trip):
                    trips.append(trip)
            else:
                dfs(con.arr_city, target_city, new_path, depth + 1)

    dfs(dep_station, arr_station, [], 1)
    return trips

def sortByDuration(trips, ascending=True):
    return sorted(trips, key=lambda t: t.totalDuration(), reverse=not ascending)

def sortByPrice(trips, ascending=True, first_class=False):
    return sorted(trips, key=lambda t: t.calculatePrice(first_class=first_class), reverse=not ascending)

def printTrips(trips, limit=None):
    """Nicely print trips; returns nothing. limit=None prints all."""
    if not trips:
        print("No trips found.")
        return
    if limit:
        trips = trips[:limit]
    for i, t in enumerate(trips, start=1):
        print(f"{i}. {t}")

# every train of the trip must be trainType for this to return something
def filterByTrainType(trainType, trips):
    filteredList = []
    for trip in trips:
        boo = True
        for connection in trip.connections:
            if connection.train_type != trainType:
                boo = False
                break
        if boo:
            filteredList.append(trip)
    return filteredList

# every corresponding dayOfWeek of the trip must be true for this to return something
def filterByDayOfWeek(dayOfWeek, trips):
    filteredList = []
    for trip in trips:
        boo = True
        for connection in trip.connections:
            if connection.days[dayOfWeek] == False:
                boo = False
                break
        if boo:
            filteredList.append(trip)
    return filteredList

'''
#User searches for a trip from A--> B for example (could be direct or indirect- 1 or 2 stops)
def searchForConnections(dep_station, arr_station):
    print("this function searches and displays the possible connection results from A to B")
'''
