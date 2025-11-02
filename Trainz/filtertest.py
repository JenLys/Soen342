# i need reference to test output of recorddb
from recorddb import RecordsDB
import tripsearch as ts
import supportfunctions as sf


file = "Trainz/eu_rail_network.csv"
# now this is connections database
db = RecordsDB(file)
cons = db.loadCsvData(file)
print(cons)
sdir = ts.getConnections('Amiens', 'Rouen', cons)
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

# me when things i expect to work stop working...
# WHY IS IT A CLASS NOW? HUH???
# and why is the original csvRead gone huh.



