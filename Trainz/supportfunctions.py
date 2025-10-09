import csv
from connection import Connection

# error ignore just skips if its not correct characters lol
# anyway this function is just to get the database
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

# converting a [] list to connection cuz lazy to redo functions
def convertRecords(listed):
    records = []
    for row in listed:
        records.append(Connection(row))

    return records

def printDirConnectionsDB(db):
    for row in db:
        print("")
        print("Route ID: " + row[0] + " leaving from " + row[1] + " at " + row[3])
        print("will arrive at " + row[2] + " at " + row[4])
        print("This is a " + row[5] + " train running on " + row[6])
        print("First class price: " + row[7] + "$ && normal price: " + row[8] + "$")
        
def printDirConnections(connect):
    for con in connect:
        print("")
        print("Route ID: " + con.route_id + " leaving from " + con.dep_city + " at " + con.dep_time)
        print("will arrive at " + con.arr_city + " at " + con.arr_time)
        print("This is a " + con.train_type + " train running on ")
        print(con.op_days)
        print("First class price: " + con.fclass_rate + "$ && normal price: " + con.sclass_rate + "$")


