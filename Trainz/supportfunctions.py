import csv
from connection import Connection

# error ignore = skips if its not correct characters
# anyway this function is just to get the database
# returns a list of list [], every row matches csv row
def csvDB(file):
    with open(file, 'r', errors='ignore') as dbIN:
        reader = csv.reader(dbIN)
        data = list(reader)
    return data

def getRecords(file):
    data = csvDB(file)
    records = []

    for row in data:
        records.append(Connection(row))

    return records

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



#Are we allowed to have supportfuncitons.py if it's not mentioned in our models and diagrams? shouldn't the loadCsvData( csvfile) be in our console?
