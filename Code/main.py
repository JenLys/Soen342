import supportfunctions
import stations

testfile = "smol.csv"
file = "eu_rail_network.csv"
# practically just copied a few rows of data to test functions

dataDB = supportfunctions.csvDB(testfile)
for row in dataDB:
    print(row)

# ngl main feels like a "test.py" file rn lol
# but heyy unit testing, unit testing

innit = stations.inputCheck("meow", "mew")
print(innit)
bruv = stations.inputCheck("Amiens", "Berlin")
print(bruv)
searchdirect = stations.listDirectORdepartures('Amiens', 'Rouen', dataDB)
searchindirect = stations.listDirectORdepartures('Amsterdam', 'Odense', dataDB)

print(searchdirect)
print(searchindirect)
print("splitting the indirect dbs into departure then destination")
print(searchindirect[0])
print(searchindirect[1])