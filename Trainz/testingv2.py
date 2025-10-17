import supportfunctions as sf
import stations
import recordDB
import tripsearch as ts


testfile = "Trainz/smol.csv"
file = "Trainz/eu_rail_network.csv"
dataDB = recordDB.csvRead(file)

searchdirect = stations.listDirectORdepartures('Amiens', 'Rouen', dataDB)
searchindirectfail = stations.listDirectORdepartures('Amsterdam', 'Odense', dataDB)
searchonestop = stations.listDirectORdepartures('Alicante', 'Granada', dataDB)
searchtwostop = stations.listDirectORdepartures('Amiens', 'Ghent', dataDB)

print("direct: 'Amiens' - 'Rouen'")
sf.functionToCheck(searchdirect, dataDB)

print("")
print("indirect 404: 'Amsterdam' - 'Odense'")
sf.functionToCheck(searchindirectfail, dataDB)

print("")
print("indirect one stop: 'Alicante' - 'Granada'")
sf.functionToCheck(searchonestop, dataDB)

print("")
print("indirect two stop: 'Amiens' - 'Ghent'")
sf.functionToCheck(searchtwostop, dataDB)

print("#######################################")
print("#######################################")
print("connection version below")
print("#######################################")
print("#######################################")


# annnd i need to write print tests for the connections too ugh
# off to the recycling binnnn

# now this is connections database
cons = recordDB.loadCsvData(file)
sdir = ts.searchTrips('Amiens', 'Rouen', cons)
sif = ts.searchTrips('Amsterdam', 'Odense', cons)
sos = ts.searchTrips('Alicante', 'Granada', cons)
sts = ts.searchTrips('Amiens', 'Ghent', cons)

print("direct: 'Amiens' - 'Rouen'")
boo1 = sdir[0]
print(boo1[0],boo1[1],boo1[2])
print("direct")
sf.printConnections(sdir[1])
print("one stop first")
sf.printConnections(sdir[2])
print("one stop last")
sf.printConnections(sdir[3])
print("two stop start")
sf.printConnections(sdir[4])
print("two stop middle")
sf.printConnections(sdir[5])
print("two stop end")
sf.printConnections(sdir[6])

print("")
print("indirect 404: 'Amsterdam' - 'Odense'")

boo2 = sif[0]
print(boo2[0],boo2[1],boo2[2])
print("direct")
sf.printConnections(sif[1])
print("one stop first")
sf.printConnections(sif[2])
print("one stop last")
sf.printConnections(sif[3])
print("two stop start")
sf.printConnections(sif[4])
print("two stop middle")
sf.printConnections(sif[5])
print("two stop end")
sf.printConnections(sif[6])

print("")
print("indirect one stop: 'Alicante' - 'Granada'")

boo3 = sos[0]
print(boo3[0],boo3[1],boo3[2])
print("direct")
sf.printConnections(sos[1])
print("one stop first")
sf.printConnections(sos[2])
print("one stop last")
sf.printConnections(sos[3])
print("two stop start")
sf.printConnections(sos[4])
print("two stop middle")
sf.printConnections(sos[5])
print("two stop end")
sf.printConnections(sos[6])

print("")
print("indirect two stop: 'Amiens' - 'Ghent'")

boo4 = sts[0]
print(boo4[0], boo4[1], boo4[2])
print("direct")
sf.printConnections(sts[1])
print("one stop first")
sf.printConnections(sts[2])
print("one stop last")
sf.printConnections(sts[3])
print("two stop start")
sf.printConnections(sts[4])
print("two stop middle")
sf.printConnections(sts[5])
print("two stop end")
sf.printConnections(sts[6])
