from connection import Connection

# converting a [] list to connection
def convertRecords(listed):
    records = []
    for row in listed:
        records.append(Connection(row))

    return records

# testing print 1
def printDirConnectionsDB(dbList):
    for row in dbList:
        print("")
        print("Route ID: " + row[0] + " leaving from " + row[1] + " at " + row[3])
        print("will arrive at " + row[2] + " at " + row[4])
        print("This is a " + row[5] + " train running on " + row[6])
        print("First class price: " + row[7] + "$ && normal price: " + row[8] + "$")
        
# testing print 2 using connections
def printDirConnections(connect):
    for con in connect:
        print("")
        print("Route ID: " + con.route_id + " leaving from " + con.dep_city + " at " + con.dep_time)
        print("will arrive at " + con.arr_city + " at " + con.arr_time)
        print("This is a " + con.train_type + " train running on ")
        print(con.op_days)
        print("First class price: " + con.fclass_rate + "$ && normal price: " + con.sclass_rate + "$")


