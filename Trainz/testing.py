# just moving stuff from main to here, UI is happening

import stationsDB
import supportfunctions
import stations
import recordDB
# import connection

testfile = "Trainz/smol.csv"
file = "Trainz/eu_rail_network.csv"
# copied a few rows of data to test functions

dataDB = recordDB.csvRead(file)

#for row in dataDB:
#    print(row)

innit = stationsDB.inputCheck("notstation", "Berlin")
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
# search indirect departure
for sid in searchindirect[1]:
    print(sid)
print("arrivals")
# search indirect arrival
for sia in searchindirect[2]:
    print(sia)

supportfunctions.functionToCheck(searchdirect, dataDB)
print("")
print("indirect")
supportfunctions.functionToCheck(searchindirect, dataDB)
print("")
print("one stop")
searchonestop = stations.listDirectORdepartures('Alicante', 'Granada', dataDB)
supportfunctions.functionToCheck(searchonestop, dataDB)
