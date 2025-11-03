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
        """Sum durations of each connection in minutes. Handles overnight (arrival earlier than departure -> +24h)."""
        total = 0
        for c in self.connections:
            dep_min = self._parse_time_minutes(c.dep_time)
            arr_min = self._parse_time_minutes(c.arr_time)
            dur = arr_min - dep_min
            if dur < 0:
                dur += 24 * 60
            total += dur
        return total

    def stops(self):
        return len(self.connections) - 1

    def __str__(self):
        path = " → ".join([c.dep_city for c in self.connections] + [self.connections[-1].arr_city])
        price = self.calculatePrice(first_class=False)
        hours = self.totalDuration() // 60
        mins = self.totalDuration() % 60
        return f"{path} | {len(self.connections)} leg(s) | {hours}h{mins}m | €{price:.2f}"


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
                trips.append(Trip(new_path))
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
