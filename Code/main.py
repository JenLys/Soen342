import connections

testfile = "smol.csv"
file = "eu_rail_network.csv"
# practically just copied a few rows of data to test functions

data = connections.csvDB(file)
for row in data:
    print(row)
