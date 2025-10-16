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

# printing one stops
def printOneStopDB(first, second):
    print(">> (one stop) two connections are")
    print("first: ")
    for row in first:
        print(row)
    print("second: ")
    for row in second:
        print(row)
    print(">> one stop end")
# function that splits the search (direct or indirect)

def printTwoStopDB(first, second, third):
    print(">> (two stop) three connections are")
    print("first")
    for row in first:
        print(row)
    print("middle")
    for row in second:
        print(row)
    print("last")
    for row in third:
        print(row)
    print(">> two stop end")

def functionToCheck(dbFound, dbcsv):
    if(dbFound[0] == "direct"):
        # print out direct connections since we have them
        printDirConnectionsDB(dbFound[1])
    elif(dbFound[0] == "indirect"):
        # search for indirect connections pt.2
        # call function with dbFound[1], dbFound[2]
        indirectFind(dbFound[1], dbFound[2], dbcsv)

# function that splits the indirect into one stop or two stop
def indirectFind(dbdep, dbarr, dbcsv):
    # dbcsv only used if 2 level search
    # lets edit the deadcode from previous stationsDB! knew it'd be useful again
    # first getting a two lists to check if overlapping stations (for 1 stop)
    uniquedepart = []
    for row in dbdep:
        if row[2] not in uniquedepart:
            uniquedepart.append(row[2])
    # non repeating list of cities you can reach from departure city
    uniquearrive = []
    for row in dbarr:
        if row[1] not in uniquearrive:
            uniquearrive.append(row[1])
    # non repeating list of cities that will reach arrival city
    isOneStop = False
    onestop = []
    for city in uniquearrive:
        if city in uniquedepart:
            onestop.append(city)
            isOneStop = True
    # so now we get a true/false, if one city stop we got the one stop!
    # just print out appropriate trips somehow
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
    # not bothering with returns, i just want to visually see if it worked 
    # since everything except the logic will be scrapped for connections version

    # otherwise now searching for 2 city stops
    # in the spirit of optimizing let's search for the smaller list
    lengtharr = len(uniquearrive)
    lengthdep = len(uniquedepart)

    twostoplist = []
    isArrivalArray = False
    # arrival list smaller than departure then look for arrival list, else flip
    # another function to write yay... 
    # and all of this is only to unit test logic, dependencies gonna go wild
    if lengtharr <= lengthdep:
        twostoplist = find2StopArrive(uniquearrive, dbcsv)
        isArrivalArray = True
    elif lengthdep < lengtharr:
        twostoplist = find2StopDepart(uniquedepart, dbcsv)
    # not even done coding and i already want to refactor...

    twostopfirst = []
    twostopsecond = []
    # look for unique middle city(1) of arrive list
    if isArrivalArray:
        for row in twostoplist:
            if row[1] in uniquedepart:
                if row[1] not in twostopfirst:
                    twostopfirst.append(row[1])
                if row[2] not in twostopsecond:
                    twostopsecond.append(row[2])
    # look for unique middle city(2) of depart list
    else:
        for row in twostoplist:
            if row[2] in uniquearrive:
                if row[1] not in twostopfirst:
                    twostopfirst.append(row[1])
                if row[2] not in twostopsecond:
                    twostopsecond.append(row[2])

    if not twostopfirst:
        print("404 no trips found")
        return 0
    # if the logic went wrong here awake me should fix it later
#
# LOOK NEAR HERE IF SMTH BROKE 
# ABOVE AND BELOW
# Actually lets stop here i think logic component just broke down mentally
# aka i forgot
#
    #
    twostopdepart = []
    twostopmiddle = []
    twostoparrive = []
    # get the departure list
    for row in dbdep:
        if row[2] in twostopfirst:
            twostopdepart.append(row)
    # get the middle list
    for row in twostoplist:
        if row[1] in twostopfirst:
            if row[2] in twostopsecond:
                twostopmiddle.append(row)
    # get the arrival list
    for row in dbarr:
        if row[1] in twostopsecond:
            twostoparrive.append(row)
    # oh i want to refactor soo bad 
    # but this is future scrap
    # anw itsa repeat of look for common middleman- middlecity and append to lists
    printTwoStopDB(twostopdepart, twostopmiddle, twostoparrive)

# arrival list was smaller, meaning we find all the middle link that will arrive to the list of cities that'll arrive to og arrival
# departure city - middeparture - THIS.midarrive/searchListArr - arrival city
# THIS is the input, now we find and return every arrival within that list 
def find2StopArrive(searchListArr, dataDBcsv):
    outrows = []
    for row in dataDBcsv:
        if row[2] in searchListArr:
            outrows.append(row)
    return outrows

# departure list was smaller, meaning we find all the middle link that will leave from the cities that can be reached from og departure icantenglish
# departure city - THIS.middeparture/searchListDep - midarrive - arrival city
# THIS is the input, now we find and return every depart within that list 
def find2StopDepart(searchListDep, dataDBcsv):
    outrows = []
    for row in dataDBcsv:
        if row[1] in searchListDep:
            outrows.append(row)
    return outrows

