import time
import sys
import stations
import stationsDB
import connection
import os
import recorddb
import results
from recorddb import RecordsDB #import the class

dir = os.path.dirname(__file__) 
#testfile = dir + "/smol.csv"
file = dir + "/eu_rail_network.csv"
# practically just copied a few rows of data to test functions

#NOTE: at the very end, once all is done we can refactor code and make the Interface code cleaner- while loop instead of ifs
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

    print("Follow the instructions to search for a trip \n" \
    "_______________________________________________ \n")
    sys.stdout.flush()
    input("Press Enter to continue...")
    
    #user's information--this is the booker (difference between booker_fname and fname for example
    #  is that a booker can book for a family member and enter the latter's lname)
    booker_input = input("Enter your last name, first name and userid (no space-split them up with commas): ")
    booker_lname, booker_fname, user_id = [x.strip() for x in booker_input.split(",")] #we are assuming a perfect user here

    dep_station = input("Where are you departing from? (enter initial station name): ")
    arr_station = input("What is your destination? (enter final station name): ")
    db = RecordsDB(file)
    
    # search for trips (returns list of Trip objects)
    trips = results.searchForConnections(db, dep_station, arr_station, max_depth=5)
    #call search method
    if not trips:
        print("\nNo routes found between those cities.\n")
    else:
        print(f"\nFound {len(trips)} possible trip(s):\n")
        results.printTrips(trips, limit=20)  # limit to first 20 for readability

    #trip.searchForConnections(dep_station, arr_station)
    

    #once the search method is done, ask the user if they wish to sort
    user_feedback_sort = input("Do you wish to sort the results? 'y' for yes, 'n' for no : ")
    if (user_feedback_sort == "y" or user_feedback_sort =="yes" or user_feedback_sort == "Y"):
        #ask for sort type, call corresponding methods
        sort_type = int(input(
        "1 - Sort by duration (ascending)\n"
        "2 - Sort by price (ascending)\n" ))

        #call the appropriate sorting function
        match sort_type:
            case 1:
                print("Results sorted from shortest to longest duration: \n")
                #call trip.sortByDuration() sort function
                results.printTrips(results.sortByDuration(trips), limit=20)
                
                
            case 2:
                print("Results sorted from lowest to highest price: \n")
                results.printTrips(results.sortByPrice(trips), limit=20)
                
            case _:
                print("Invalid entry. Returning back to the main menu...")
                time.sleep(3)
                printMenu()

        user_feedback_return = input("Do you wish to do a new operation (back to menu)? 'y' for yes, 'n' for no: ")
        if (user_feedback_return == "y" or user_feedback_return == "yes" or user_feedback_return == "Y"):
            printMenu()
        else:
            askbooking()
            print("Thank you for using Trainz System")
            sys.exit(0)
        

    else:
        askbooking()
        user_feedback_return = input("Return to main menu? 'y' for yes, 'n' for no: ")
        if (user_feedback_return == "y" or user_feedback_return == "yes" or user_feedback_return == "Y"):
            printMenu()
        else:
            print("Thank you for using Trainz System")
            sys.exit(0)


    
  

    ''' FOR THE FUTURE ITERATION, ADD MORE SEARCH FILTERS. here iteration 1: our models only have 2 possible search parameters, add more for Iteration2
    print("1. Search by departure or arrival station")
    print("2. Search by departure or arrival time")
    print("3. Search by train type")
    print("4. Search by days of operation")
    print("5. Search by ticket rate (First and Second class)")
    '''
#This function does the console interface work when the user wants to book a trip
def askbooking():
    booking_req_input = input("Do you wish to do a booking? 'y' for yes, 'n' for no: ")
    if (booking_req_input == "y" or booking_req_input == "yes" or booking_req_input == "Y"):
        
        while True:
            #user provides user info in order to book (name, id, age, ...)
            booking_user_info = input("Please identify yourself to proceed with the booking: first name,last name,age,id  (*commas included with no space): ")
            #in case the user enters gibberish, try catch
            try:
                fields = booking_user_info.split(",") #extracts fields split by ,
                #extra info added, reject
                if len(fields) != 4:
                    print("The system was not able to identify you. Please try again \n")
                    askbooking
                
                fname, lname, age, user_id = fields #assigned in order
                #validate type (positive age only, can add more filters later)
                age_input = int(age)
                if age_input <= 0:
                    print("You have entered an invalid age. Try again...\n")
                    askbooking
                break 

            except ValueError as e:
                print("The system was not able to identify you. Please try again")
                printMenu

    else: #user replies No or something else
        print("Redirecting to Trainz System... \n")
        printMenu

def main():
    #call on to load csv data
    
    db = RecordsDB(file)
    print(f"Loaded {len(db.getAllConnections())} connections...")

    #test out, print first 5 connections
    for c in db.getAllConnections()[:5]:
        print(c)

    #call method to print menu
    printMenu()
   

   
    '''
    while(True):
        printMenu()
        menu_choice = input("Select: ")
        print("Choose departure and arrival stations to book your trip:")
        dep_station = input("Departure Station: ")
        arr_station = input("Arrival Station: ")
    

    records = recorddb.loadCsvData(file)

    for r in records:
       print(r.route_id, r.op_days)
    '''

if __name__ == "__main__":
    main()