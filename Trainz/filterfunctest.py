import os
import results
from results import Trip
from recordDB import RecordsDB #import the class
import filterfunction as ff

dir = os.path.dirname(__file__)
file = dir + "/eu_rail_network.csv"

dep_station = "Amiens"
arr_station = "Rouen"
db = RecordsDB(file)

# search for trips (returns list of Trip objects)
trips = results.searchForConnections(db, dep_station, arr_station, max_depth=2)
#call search method
i = 0
if not trips:
    print("\nNo routes found between those cities.\n")
else:
    print(f"\nFound {len(trips)} possible trip(s):\n")
    for t in trips:
        print(i)
        for tt in t.connections:
            print(tt)
        i += 1

i = 0
print("train type filter?\n")
tr = ff.filterByTrainType("EuroCity", trips)
if not tr:
    print("\nNo routes found with that filter.\n")
else:
    print(f"\nFound {len(trips)} possible trip(s):\n")
    for t in tr:
        print(i)
        for tt in t.connections:
            print(tt)
        i += 1

i = 0
print("\nday of week filter?\n")
tra = ff.filterByDayOfWeek("Mon", trips)
if not tra:
    print("\nNo routes found with that filter.\n")
else:
    print(f"\nFound {len(trips)} possible trip(s):\n")
    for t in tra:
        print(i)
        for tt in t.connections:
            print(tt)
        i += 1
