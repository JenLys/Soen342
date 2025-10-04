ok basically what things do
####### TLDR AT END

if you run main, that's where tested functions are so far

supportfunctions: just reads csv file and translates into a list of lists
(was formerly in connections, but it made no sense so moved it)

stationsDB: we have the component in diagram, so hardcoded it, just pulled every city name from the departure column, the dead code that did that is commented

stations: 
function one the sanity check of if the inputs are correct (one fears the weird characters)
function two gets the departure(start), the destination(end), and the database as parameters and spits out
    - either a list of direct trips
    - or a list made of 2 lists of which
        - list 1 has all the matching STARTs of the search (every train that leaves the station)
        - list 2 has all the matching ENDs of the search (every train that enters the destination station)
Meaning whoever wrote this code is hoping to find a direct trip or a one stop trip from the above data. ((Definitely not copium))


####### To do:
- figure out which entity should be doing what
- get the connection logic
- get the 2 stop logic (good luck to whoever's gonna do this -afk)
- get some sorting logic for time and money
- frontend? ui? 


####### TLDR:
main.py: testing functions
supportfunctions.py: csv file => list of lists
stationsDB.py: hardcoded list of all stations
stations.py: (function 1) input validation
    (function 2) list of direct trips 
    OR 
    SQL-style return of 2 lists
        list 1: trips that start from searched departure
        list 2: trips that end up at searched destination
Timestamp: oct-4, almost 7am, wtf is a sleep schedule