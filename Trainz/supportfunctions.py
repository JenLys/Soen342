import csv
from Trainz.connection import Connection

# error ignore just skips if its not correct characters lol
# anyway this function is just to get the database
def csvDB(file):
    with open(file, 'r', errors='ignore') as dbIN:
        reader = csv.reader(dbIN)
        data = list(reader)
    return data

def getRecords(file):
    data = csvDB(file)
    records = []

    for row in data:
        records.append(Connection(row))

    return records


#Are we allowed to have supportfuncitons.py if it's not mentioned in our models and diagrams? shouldn't the loadCsvData( csvfile) be in our console?