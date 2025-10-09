# just moving stuff from main to here cuz UI is happening

import stationsDB
import supportfunctions
import stations
# import connection

testfile = "Trainz/smol.csv"
file = "Trainz/eu_rail_network.csv"
# practically just copied a few rows of data to test functions

dataDB = supportfunctions.csvDB(testfile)

#for row in dataDB:
#    print(row)

    # ngl main feels like a "test.py" file rn lol
    # but heyy unit testing, unit testing

innit = stationsDB.inputCheck("meow", "mew")
print(innit)
bruv = stationsDB.inputCheck("Amiens", "Berlin")
print(bruv)

searchdirect = stations.listDirectORdepartures('Amiens', 'Rouen', dataDB)
searchindirect = stations.listDirectORdepartures('Amsterdam', 'Odense', dataDB)
print(searchdirect[0])
for sd in searchdirect[1]:
    print(sd)

# prints from db
supportfunctions.printDirConnectionsDB(searchdirect[1])

# make into connnection then print?
contest = supportfunctions.convertRecords(searchdirect[1])
supportfunctions.printDirConnections(contest)

print()
print("splitting the indirect dbs into departure then destination")
print(searchindirect[0])
print()
print("departures")
for sid in searchindirect[1]:
    print(sid)
print("arrivals")
for sia in searchindirect[2]:
    print(sia)

