import time
import sys
import stations
import stationsDB
import connection
import os
import recorddb
import results
from recorddb import RecordsDB #import the class

dir = os.path.dirname(__file__) 
#testfile = dir + "/smol.csv"
file = dir + "/eu_rail_network.csv"

dep_station = "Amiens"
arr_station = "Rouen"
db = RecordsDB(file)

# search for trips (returns list of Trip objects)
trips = results.searchForConnections(db, dep_station, arr_station, max_depth=2)
#call search method
if not trips:
    print("\nNo routes found between those cities.\n")
else:
    print(f"\nFound {len(trips)} possible trip(s):\n")
    results.printTrips(trips, limit=200)  # limit to first 20 for readability

