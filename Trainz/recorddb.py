import csv
from connection import Connection

# error ignore just skips if its not correct characters lol
# anyway this function is just to get the database
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