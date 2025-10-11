import csv
from connection import Connection

# error ignore, skips if its not correct characters
# anyway this function is to get the database
def csvRead(file):
    with open(file, 'r', errors='ignore') as dbIN:
        reader = csv.reader(dbIN)
        data = list(reader)
    return data

def loadCsvData(file):
    data = csvRead(file)
    records = []

    for row in data:
        records.append(Connection(row))

    return records

class RecordsDB:
    def __init__(self, file):
        connections = loadCsvData(file)
#testing branch protection


#User searches for a trip from A--> B for example (could be direct or indirect- 1 or 2 stops)
def searchForConnections(dep_station, arr_station):
    print("this function searches and displays the possible connection results from A to B")
    