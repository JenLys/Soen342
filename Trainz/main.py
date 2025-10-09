import supportfunctions
import stations
import stationsDB
import connection

def printMenu():
    print("Choose trip search parameters: ")
    print("1. Search by departure or arrival station")
    print("2. Search by departure or arrival time")
    print("3. Search by train type")
    print("4. Search by days of operation")
    print("5. Search by ticket rate (First and Second class)")

def main():
    '''
    while(True):
        printMenu()
        menu_choice = input("Select: ")
        print("Choose departure and arrival stations to book your trip:")
        dep_station = input("Departure Station: ")
        arr_station = input("Arrival Station: ")
    '''

    records = supportfunctions.getRecords("Trainz/eu_rail_network.csv")

    for r in records:
        print(r.route_id, r.op_days)

if __name__ == "__main__":
    main()