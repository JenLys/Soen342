import connection

# for the big function in here: grabbed the one function in station too, so that one can begone now tbh

# in: String departure, String arrival, list of connections/database
# out: list of lists
# [0] list of 3 booleans
    # [0] hasDirect
    # [1] hasOneStop
    # [2] hasTwoStop
# [1] list of direct connection(s)
# [2] list of one stop - first connection(s)
# [3] list of one stop - last connection(s)
# [4] list of two stop - start connection(s)
# [5] list of two stop - middle connection(s)
# [6] list of two stop - end connection(s)
# PLS READ: [1][2][3][4][5][6] may be empty
    # if all booleans are False 
# for an idea of what the output looks like w minimal processing, run the current testingv2.py and think of the rows pulled from database as connections. or look on discord/off-topic. whatever
# also recommended to open var explanation txt while reading if anyone wants to suffer through that
def searchTrips(departure, arrival, connectionlist):
    direct = []
    indirectdepartures = []
    indirectarrivals = []
    # if there's direct connection, gets the list of direct connections
    # if no direct connections, gets the list of all trips leaving from departure & reaching arrival
    hasDirect = False
    for row in connectionlist:
        # if departure city matches with search
        if row.dep_city == departure:
            # and also matches with arrival search
            if row.arr_city == arrival:
                direct.append(row)
                hasDirect = True
                # get in the direct
            else:
                indirectdepartures.append(row)
        # otherwise only destination matches with search
        elif row.arr_city == arrival:
            # get in the indirect destination
                indirectarrivals.append(row)
    # direct and first indirect layer done
    # -----------------------------------------
    # non repeating list of stations you can reach from departure city
    firstMiddleStations = getArrivalStations(indirectdepartures)
    # non repeating list of stations that will reach arrival city
    secondMiddleStations = getDepartureStations(indirectarrivals)
    # -----------------------------------------
    onestopdepart = []
    onestoparrive = []
    # now checking the two lists to check if overlapping stations (for 1 stop)
    onestop = []
    for station in firstMiddleStations:
        if station in secondMiddleStations:
            if station not in onestop:
                onestop.append(station)
    
    hasOneStop = False
    # if onestop has even one value, it'll be True
    if onestop:
        hasOneStop = True
        # get the departure list
        for row in indirectdepartures:
            if row.arr_city in onestop:
                onestopdepart.append(row)
        # get the arrival list
        for row in indirectarrivals:
            if row.dep_city in onestop:
                onestoparrive.append(row)
    # -----------------------------------------
    # now searching for 2 city stops
    # in the spirit of optimizing, search for the smaller list
    lengthdep = len(firstMiddleStations)
    lengtharr = len(secondMiddleStations)
    twostoplist = []
    isArrivalArray = False
    # arrival list smaller than departure then look for arrival list, else flip
    if lengtharr <= lengthdep:
        twostoplist = find2StopArrive(secondMiddleStations, connectionlist)
        isArrivalArray = True
    elif lengthdep < lengtharr:
        twostoplist = find2StopDepart(firstMiddleStations, connectionlist)
    # those two are the cities that actually connect if they exist
    twostopfirst = []
    twostopsecond = []
    # look for unique middle city(1) of arrive list
    if isArrivalArray:
        for row in twostoplist:
            if row.dep_city in firstMiddleStations:
                if row.dep_city not in twostopfirst:
                    twostopfirst.append(row.dep_city)
                if row.arr_city not in twostopsecond:
                    twostopsecond.append(row.arr_city)
    # look for unique middle city(2) of depart list
    else:
        for row in twostoplist:
            if row.arr_city in secondMiddleStations:
                if row.dep_city not in twostopfirst:
                    twostopfirst.append(row.dep_city)
                if row.arr_city not in twostopsecond:
                    twostopsecond.append(row.arr_city)
    # end of optimization divergence
    # -----------------------------------------
    # try to find if there are two stops & add them to the 3 lists
    hasTwoStop = False
    if twostopfirst:
        hasTwoStop = True

    twostopdepart = []
    twostopmiddle = []
    twostoparrive = []

    if hasTwoStop:
        # get the departure list
        for row in indirectdepartures:
            if row.arr_city in twostopfirst:
                twostopdepart.append(row)
        # get the middle list
        for row in twostoplist:
            if row.dep_city in twostopfirst:
                if row.arr_city in twostopsecond:
                    twostopmiddle.append(row)
        # get the arrival list
        for row in indirectarrivals:
            if row.dep_city in twostopsecond:
                twostoparrive.append(row)

    bools = [hasDirect, hasOneStop, hasTwoStop]
    return(bools, direct, onestopdepart, onestoparrive, twostopdepart, twostopmiddle, twostoparrive)


# returns unique departure stations list
def getDepartureStations(connect):
    out = []
    for c in connect:
        if c.dep_city not in out:
            out.append(c.dep_city)
    return out

# returns unique arrival stations list
def getArrivalStations(connect):
    out = []
    for c in connect:
        if c.arr_city not in out:
            out.append(c.arr_city)
    return out

# arrival list was smaller, meaning we find all the middle link that will arrive to the list of cities that'll arrive to og arrival
# departure city - middeparture - THIS.midarrive/searchListArr - arrival city
# THIS is the input, now we find and return every arrival within that list 
def find2StopArrive(searchListArr, dataDBcsv):
    outrows = []
    for row in dataDBcsv:
        if row.arr_city in searchListArr:
            outrows.append(row)
    return outrows

# departure list was smaller, meaning we find all the middle link that will leave from the cities that can be reached from og departure icantenglish
# departure city - THIS.middeparture/searchListDep - midarrive - arrival city
# THIS is the input, now we find and return every depart within that list 
def find2StopDepart(searchListDep, dataDBcsv):
    outrows = []
    for row in dataDBcsv:
        if row.dep_city in searchListDep:
            outrows.append(row)
    return outrows
