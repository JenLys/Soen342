from stationsDB import citystations

# sanity check if proper city  input
def inputCheck(departure, destination):
    if departure in citystations:
        if destination in citystations:
            return True
        else:
            return False
    else:
        return False

# if there's direct trip, returns the list of direct trips
# if no direct trip, returns the list of all trips departing from spot
def listDirectORdepartures(departure, destination, dblist):
    indirectdepartures = []
    direct = []
    indirectdestinations = []
    flagging = False
    # parse row by row
    for row in dblist:
        # if departure city matches with search
        if row[1] == departure:
            # and also matches with destination search
            if row[2] == destination:
                # means direct trips are ON, so flag to return direct
                direct.append(row)
                flagging = True
            elif flagging:
                pass
            # get in the departure van
            else:
                indirectdepartures.append(row)
        # otherwise only destination matches with search
        elif row[2] == destination:
            # direct trips are on, skip
            if flagging:
                pass
            # get them in the indirect destination gang
            else:
                indirectdestinations.append(row)


    if flagging:
        return direct

    return (indirectdepartures, indirectdestinations)


