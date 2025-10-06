import supportfunctions
import stations
import stationsDB

testfile = "Code/smol.csv"
file = "Code/eu_rail_network.csv"
# practically just copied a few rows of data to test functions

def printMenu():
    print("Select an Option:")
    print("1. ")

def main():
    dataDB = supportfunctions.csvDB(testfile)
    for row in dataDB:
        print(row)

    # ngl main feels like a "test.py" file rn lol
    # but heyy unit testing, unit testing

    innit = stationsDB.inputCheck("meow", "mew")
    print(innit)
    bruv = stationsDB.inputCheck("Amiens", "Berlin")
    print(bruv)

    searchdirect = stations.listDirectORdepartures('Amiens', 'Rouen', dataDB)
    searchindirect = stations.listDirectORdepartures('Amsterdam', 'Odense', dataDB)
    print(searchdirect)
    print(searchindirect)
    print("splitting the indirect dbs into departure then destination")
    print(searchindirect[0])
    print(searchindirect[1])
    print(searchindirect[2])

    records = supportfunctions.getRecords("Code/eu_rail_network.csv")

    while(True):
        printMenu()
        option = input("Select: ")


if __name__ == "__main__":
    main()