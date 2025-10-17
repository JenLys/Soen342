import supportfunctions
import stations
import recordDB

testfile = "Trainz/smol.csv"
file = "Trainz/eu_rail_network.csv"
dataDB = recordDB.csvRead(file)

searchdirect = stations.listDirectORdepartures('Amiens', 'Rouen', dataDB)
searchindirectfail = stations.listDirectORdepartures('Amsterdam', 'Odense', dataDB)
searchonestop = stations.listDirectORdepartures('Alicante', 'Granada', dataDB)
searchtwostop = stations.listDirectORdepartures('Amiens', 'Ghent', dataDB)

print("direct: 'Amiens' - 'Rouen'")
supportfunctions.functionToCheck(searchdirect, dataDB)

print("")
print("indirect 404: 'Amsterdam' - 'Odense'")
supportfunctions.functionToCheck(searchindirectfail, dataDB)

print("")
print("indirect one stop: 'Alicante' - 'Granada'")
supportfunctions.functionToCheck(searchonestop, dataDB)

print("")
print("indirect two stop: 'Amiens' - 'Ghent'")
supportfunctions.functionToCheck(searchtwostop, dataDB)


# annnd i need to write print tests for the connections too ugh