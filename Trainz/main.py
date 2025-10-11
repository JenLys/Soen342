import time
import sys
import stations
import stationsDB
import connection
import os
import recorddb

dir = os.path.dirname(__file__) 
testfile = dir + "/smol.csv"
file = dir + "/eu_rail_network.csv"
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

    print("Follow the instructions to search for a trip \n" \
    "_______________________________________________ \n")
    dep_station = input("Where are you departing from? (enter initial station name): ")
    arr_station = input("What is your destination? (enter final station name): ")
    recorddb.searchForConnections(dep_station, arr_station)
    #call search method

    #once the search method is done, ask the user if they wish to sort
    user_feedback_sort = input("Do you wish to sort the results? 'y' for yes, 'n' for no : ")
    if (user_feedback_sort == "y" or user_feedback_sort =="yes" or user_feedback_sort == "Y"):
        #ask for sort type, call corresponding Recorddb methods
        sort_type = int(input(
        "1 - Sort by duration (ascending)\n"
        "2 - Sort by price (ascending)\n" ))

        #call the appropriate sorting function
        match sort_type:
            case 1:
                print("Results sorted from shortest to longest duration: \n")
                #call recorddb.sortByDuration() sort function
                
            case 2:
                print("Results sorted from lowest to highest price: \n")
                #call recorddb.sortByPrice() sort function
                
            case _:
                print("Invalid entry. Returning back to the main menu...")
                time.sleep(3)
                printMenu()

        user_feedback_return = input("Do you wish to do a new operation (back to menu)? 'y' for yes, 'n' for no: ")
        if (user_feedback_return == "y" or user_feedback_return == "yes" or user_feedback_return == "Y"):
            printMenu()
        else:
            print("Thank you for using Trainz System")
            sys.exit(0)
        

    else:
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

def main():
    #call on to load csv data

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