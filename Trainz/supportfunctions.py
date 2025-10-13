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

def printOneStopDB(first, second):
    print("the first connection(s) are: ")
    for row in first:
        print(row)
    print("the second connection(s) are: ")
    for row in second:
        print(row)
    

def functionToCheck(dbFound):
    if(dbFound[0] == "direct"):
        # print out direct connections since we have them
        printDirConnectionsDB(dbFound[1])
    elif(dbFound[0] == "indirect"):
        # search for indirect connections pt.2
        # call function with dbFound[1], dbFound[2]
        indirectFind(dbFound[1], dbFound[2])

def indirectFind(dbdep, dbarr):
    # lets edit the deadcode from previous stationsDB! knew it'd be useful again
    # first getting a two lists to check if overlapping stations (for 1 stop)
    uniquedepart = []
    for row in dbdep:
        if row[2] not in uniquedepart:
            uniquedepart.append(row[2])
    # print(uniquedepart)
    # non repeating list of cities you can reach from departure city
    uniquearrive = []
    for row in dbarr:
        if row[1] not in uniquearrive:
            uniquearrive.append(row[1])
    # print(uniquearrive)
    # non repeating list of cities that will reach arrival city
    isOneStop = False
    onestop = []
    for city in uniquearrive:
        if city in uniquedepart:
            onestop.append(city)
            isOneStop = True
    # so now we get a true/false, if one city stop we got the one stop! just print out appropriate trips somehow
    onestopdepart = []
    onestoparrive = []
    if (isOneStop):
        # get the departure list
        for row in dbdep:
            if row[2] in onestop:
                onestopdepart.append(row)
        # get the arrival list
        for row in dbarr:
            if row[1] in onestop:
                onestoparrive.append(row)
        #print(onestopdepart)
        #print("&")
        #print(onestoparrive)
        printOneStopDB(onestopdepart, onestoparrive)


    # otherwise now searching for 2 city stops