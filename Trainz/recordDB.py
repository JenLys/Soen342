import csv
from typing import List
from connection import Connection

# error ignore, skips if its not correct characters
# anyway this function is to get the database

def csvRead(file) -> List[List[str]]: #read csv and return rows
    with open(file, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader if any(cell.strip() for cell in row.values())]
    return rows

class RecordsDB:
    def __init__(self, file):
        #list of connection objects, that's our db
        self.connections = []
        self.loadCsvData(file)
        #connections = loadCsvData(file)
    
    def loadCsvData(self,file):
        print("Loading CSV data...")
        rows = csvRead(file)
        if not rows:
            print("No rows read from CSV.")
            return

        header = rows[0].keys()

        for row in rows:
            try:
                conn = Connection(
                    row['Route ID'],
                    row['Departure City'],
                    row['Arrival City'],
                    row['Departure Time'],
                    row['Arrival Time'],
                    row['Train Type'],
                    row['Days of Operation'],
                    row['First Class ticket rate (in euro)'],
                    row['Second Class ticket rate (in euro)']
                 )
                self.connections.append(conn)
            except Exception as e:
                print(f"Skipping row due to error: {e}")

    def getAllConnections(self): #returns all connections -list
        return self.connections

        ''' for row in data:
            records.append(Connection(row))

        return records'''
    #testing branch protection

    #get connections with specific Departure city
    def getConnectionsFrom(self, dep_city: str):
        return[c for c in self.connections if c.dep_city == dep_city]

    #get connections with specific Arrival/Destination city
    def getConnectionsTo(self, arr_city: str):
        return[c for c in self.connections if c.arr_city == arr_city]

    #find connection by routeid, it'll be a 1 to 3 id string in
    def find(self, route_id: str):
        if not route_id:
            return
        indicator = route_id[0]
        rest = route_id[1:].split("R")
        trips = []

        match indicator:
            case 'E':
                return []
            case 'U':
                totalCount = 1
                one = "R"+rest[1] # because [0] is empty somehow
                routesIDs = [one]
            case 'D':
                totalCount = 2
                one = "R"+rest[1]
                two = "R"+rest[2]
                routesIDs = [one, two]
            case 'T':
                totalCount = 3
                one = "R"+rest[1]
                two = "R"+rest[2]
                three = "R"+rest[3]
                routesIDs = [one, two, three] 

        count = 0
        for c in self.connections:
            if c.route_id in routesIDs:
                trips.append(c)
                count = count + 1
                # if matching count, then found all trips
                if count == totalCount:
                    break
        
        match indicator:
            case 'U':
                forTrip = trips
            case 'D':
                for tr in trips:
                    if tr.route_id == one: 
                        tone = tr
                    elif tr.route_id == two:
                        ttwo = tr
                forTrip = [tone, ttwo]
            case 'T':
                for tr in trips:
                    if tr.route_id == one: 
                        tone = tr
                    elif tr.route_id == two:
                        ttwo = tr
                    elif tr.route_id == three:
                        tthree = tr
                forTrip = [tone, ttwo, tthree] 
        return forTrip

    #adding a connection to the catalog of connections
    def addConnection(self, connection: Connection):
        self.connections.append(connection)
        