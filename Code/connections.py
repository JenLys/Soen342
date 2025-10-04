import csv

# error ignore just skips if its not correct characters lol
# anyway this function is just to get the database
def csvDB(file):
    with open(file, 'r', errors='ignore') as dbIN:
        reader = csv.reader(dbIN)
        data = list(reader)
    return data


