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
    "departures": False,
    "dep_city": "",
    "arrivals": False,
    "arr_city": "",
    "trips": False,
    "traintype": False,
    "dayOfWeek": False,
    "counter": 0 # for traintype & dayOfWeek if the rest are False, because this requires database parsing if only one is active
}
# Need this to be a global variable
statesUpdatedDict = None
# And a reset to clear everything
def resetFilterStates():
    global statesUpdatedDict
    statesUpdatedDict = deepcopy(statesResetDict)

filteredList = []
allRecordDefaultList = [filteredList, statesUpdatedDict]
# how the list should work:
# 0 - current filtered, 1 - dictionary

# Initialize stuff when needed
def __init__():
    statesUpdatedDict = deepcopy(statesResetDict)