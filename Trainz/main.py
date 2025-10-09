import supportfunctions
import stations
import stationsDB
import connection

testfile = "Code/smol.csv"
file = "Code/eu_rail_network.csv"
# practically just copied a few rows of data to test functions

def printMenu(): 
    print("""
          
        /$$$$$$$$                 /$$                    
        |__  $$__/                |__/                    
          | $$  /$$$$$$  /$$$$$$  /$$ /$$$$$$$  /$$$$$$$$
          | $$ /$$__  $$|____  $$| $$| $$__  $$|____ /$$/
          | $$| $$  \__/ /$$$$$$$| $$| $$  \ $$   /$$$$/ 
          | $$| $$      /$$__  $$| $$| $$  | $$  /$$__/  
          | $$| $$     |  $$$$$$$| $$| $$  | $$ /$$$$$$$$
          |__/|__/      \_______/|__/|__/  |__/|________/ 
    """)

    print("Choose trip search parameters: ")
    
    search_type = int(input(
        "1 - Search by duration (ascending)\n"
        "2 - Search by price (ascending)\n"
    ))

    return search_type



    ''' FOR THE FUTURE ITERATION, ADD MORE SEARCH FILTERS. here iteration 1: our models only have 2 possible search parameters, add more for Iteration2
    print("1. Search by departure or arrival station")
    print("2. Search by departure or arrival time")
    print("3. Search by train type")
    print("4. Search by days of operation")
    print("5. Search by ticket rate (First and Second class)")
    '''

def main():
    '''
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

    while(True):
        printMenu()
        menu_choice = input("Select: ")
        print("Choose departure and arrival stations to book your trip:")
        dep_station = input("Departure Station: ")
        arr_station = input("Arrival Station: ")
    '''

    records = supportfunctions.getRecords("Code/eu_rail_network.csv")

    for r in records:
        print(r.route_id, r.op_days)

if __name__ == "__main__":
    main()