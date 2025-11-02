'''Pseudocode explanation of goals: 
Filtering parameters for connections
- dictionary to know which filters are active
- reset when new trip is given
default sorting will sort the entire database (very time consuming the first time)
therefore keep subsequent result in list of lists
'''
import recorddb
# Need getConnectionsFrom & getConnectionsTo

# Need deep copy for dictionary of states and useful information
from copy import deepcopy
# Initial filter states, a dictionary
statesResetDict = {
    "dep_city": "",
    "arr_city": "",
    "traintype": False,
    "dayOfWeek": False,
}
# Need this to be a global variable
statesUpdatedDict = {}
# And a reset to clear everything
def resetFilterStates():
    global statesUpdatedDict
    statesUpdatedDict = deepcopy(statesResetDict)

filteredList = []
allRecordDefaultList = []
# how the list should work:
# 0 - current filtered, 1 - dictionary

# Initialize stuff when needed
def __init__():
    global allRecordDefaultList
    allRecordDefaultList = [filteredList, statesUpdatedDict]

# every train of the trip must be trainType for it to return something
def filterByTrainType(trainType, trips):
    global filteredList
    global statesUpdatedDict

    filteredList.clear()

    for trip in trips:
        boo = True
        for connection in trip.connections:
            if connection.train_type != trainType:
                boo = False
                break
        if boo:
            filteredList.append(trip)

    return filteredList
# hmm i dont use the states... will delete

def filterByDayOfWeek(dayOfWeek, trips):
    global filteredList
    global statesUpdatedDict

    filteredList.clear()

    for trip in trips:
        boo = True
        for connection in trip.connections:
            if connection.days[dayOfWeek] == False:
                boo = False
                break
        if boo:
            filteredList.append(trip)
    return filteredList