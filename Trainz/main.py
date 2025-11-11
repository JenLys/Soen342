import sys
import os
from typing import List
from user import User
import connection
import results
from bookingDB import BookingDBClass
from reservation import Reservation
from recordDB import RecordsDB
import sqlite3
import users
import connections
import reservations
import trips
import tickets

dir = os.path.dirname(__file__) 
file = dir + "/eu_rail_network.csv"

def printTrips(con):
    choice = input("Would you like to see Trips for a given user (must be the booking user)?: ")

    if choice not in ["Y", "YES"]:
        return
    
    user_id = input("Please enter your User ID: ")

    while users.find_user(user_id) == None:
        print("User could not be found... Please try again")
        user_id = input("User ID: ")

    print("Which trips would you like to see?")
    print("1. Past")
    print("2. Current")
    print("3. All")
    choice = int(input("Choice: "))

    match choice:
        case 1:
            past_trips = trips.find_past_trips(user_id, con)
            if len(past_trips) == 0:
                print("No past trips found for given user")
            else:
                for trip in past_trips:
                    print(trip)
        case 2:
            current_trips = trips.find_current_trips(user_id, con)
            if len(current_trips) == 0:
                print("No current trips found for given user")
            else:
                for trip in current_trips:
                    print(trip)
        case 3:
            all_trips = trips.find_trips(user_id, con)
            if len(all_trips) == 0:
                print("No trips found for given user")
            else:
                for trip in all_trips:
                    print(trip)
        case _:
            print("Incorrect input, returning to main menu...")

#Function called when the user desires to make a booking (reservation of a displayed result)
def askbooking():
    booking_req_input = input("Do you wish to do a booking? 'y' for yes, 'n' for no: ")
    if (booking_req_input.capitalize() in ["Y", "YES"]):
        bookNow = input("Do you wish to book for now (current)? select y-yes or n-no if you wish to book for later: ")
        if bookNow.capitalize() in ["Y", "YES"]:
            current = True #the booked selection is for a CURRENT TRIP
        else:
            current = False # PAST TRIP

         #a person can book for themselves, or do multiple bookings (each reservation under the other name)
        num = int(input("How many people will be booking today?: "))
        print("/n")

        main_user_id = 0
        reservation_list = ""
        
        for index in range(num): #loop for each person
            while True:
                user_id = input("Please enter your user ID: ")

                user = users.find_user(user_id)
                
                if user == None:
                    booking_user_info = input("Please identify yourself to proceed with the booking: first name, last name, age: ")
                    #in case the user enters gibberish, try catch
                    try:
                        fields = booking_user_info.split(", ") #extracts fields split by ,
                        #extra info added, reject
                        if len(fields) != 3:
                            raise ValueError("The system was not able to identify you. Please try again \n")
                        
                        fname, lname, age = fields #assigned in order
                        #validate type (positive age only, can add more filters later)
                        age = int(age)
                        while age < 0:
                            age = int(input("You have entered an invalid age. Please try again: "))

                        user = User(fname, lname, user_id, age) #creates a new user and stores it in the user database
                        users.insert_user(user)

                        print("User identified, proceed to do booking...")

                    except ValueError as e:
                        print("The system was not able to identify you. Please try again")
                        continue

                    selected_option = input("Which option would you like to book? Please enter the result's id: ") #corresponds to result_id
                    reservation = BookingDBClass.create_reservation(fname,lname,age,selected_option,user_id,current)

                    if index == 0:
                        main_user_id = user_id
                        reservation_list = reservation_list + reservation.reservation_id
                    else:
                        reservation_list = ", " + reservation.reservation_id

                    break
        BookingDBClass.create_trip(main_user_id, reservation_list, current)
    #user doesn't select Yes --replies No or something else
    else: 
        print("Redirecting to Trainz System... \n")

def displayConnectionsByParameter(connections: List[connection.Connection]):
    print("1: Departure City")
    print("2: Arrival City")
    print("3: Departure Time and Date")
    print("4: Arrival Time and Date")
    print("5: Days of Operation")
    print("6: Train Type")
    print("7: First class ticket rate (Euros)")
    print("8: Second class ticket rate (Euros)")

    parameter = input("Choice (1-7): ")
    parameter = int(parameter)

    if(parameter == 3 or parameter == 4):
        print("(Enter as [Time, Date])")

    value = input("Please enter a value: ")

    if(parameter == 1):
        print(value)
        for connection in connections:
            if connection.dep_city.capitalize() == value.capitalize():
                print(connection)
    elif(parameter == 2):
        for connection in connections:
            if connection.arr_city.capitalize() == value.capitalize():
                print(connection)
    elif(parameter == 3):
        value = value.split(", ")
        for connection in connections:
            if connection.dep_time == value[0] and connection.days[value[1]]:
                print(connection)
    elif(parameter == 4):
        value = value.split(", ")
        for connection in connections:
            if connection.arr_time == value[0] and connection.days[value[1]]:
                print(connection)
    elif(parameter == 5):
        for connection in connections:
            if value.capitalize() == connection.days_str.capitalize():
                print(connection)
    elif(parameter == 6):
        for connection in connections:
            if value.capitalize() == connection.train_type.capitalize():
                print(connection)
    elif(parameter == 7):
        for connection in connections:
            if connection.fclass_rate == int(value):
                print(connection)
    elif(parameter == 8):
        for connection in connections:
            if connection.sclass_rate == int(value):
                print(connection)

def searchConnections(db: RecordsDB):
    choice = input("Would you like to search the list of connections (yes/y for yes, n for no)?: ")
    
    while(choice.capitalize() in ["YES", "Y"]):
        connections = db.getAllConnections()
        print("Which parameter would you like to search by?")
        displayConnectionsByParameter(connections)
        choice = input("Would you like to make another search?: ")

    print("...end of search")
        
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
    #booker_input = input("Enter your last name, first name and userid (no space-split them up with commas): ")
    #booker_lname, booker_fname, user_id = [x.strip() for x in booker_input.split(",")] #we are assuming a perfect user here
    db = RecordsDB(file)

    searchConnections(db)

    dep_station = input("Where are you departing from? (enter initial station name): ")
    arr_station = input("What is your destination? (enter final station name): ")

    journeys = results.searchForConnections(db, dep_station, arr_station, max_depth=3)
    #call search method
    if not journeys:
        print("\nNo routes found between those cities.\n")
    else:
        print(f"\nFound {len(journeys)} possible journey(s):\n")
        results.printJourneys(journeys, limit=20)  # limit to first 20 for readability

    #once the search method is done, ask the user if they wish to sort
    user_feedback_sort = input("Do you wish to sort the results? 'y' for yes, 'n' for no : ")
    if (user_feedback_sort == "y" or user_feedback_sort.lower() =="yes" or user_feedback_sort == "Y"):
        #ask for sort type, call corresponding methods
        sort_type = int(input(
        "1 - Sort by duration (ascending)\n"
        "2 - Sort by price (ascending)\n" 
        "3 - Filter by train type\n"
        "4 - Filter by day of the week\n"))

        #call the appropriate sorting function
        match sort_type:
            case 1:
                print("Results sorted from shortest to longest duration: \n")
                #call trip.sortByDuration() sort function
                results.printJourneys(results.sortByDuration(journeys), limit=20)      
                
            case 2:
                print("Results sorted from lowest to highest price: \n")
                results.printJourneys(results.sortByPrice(journeys), limit=20)

            case 3:
                train_type_input = input("Enter the train type you wish to filter by (e.g., EuroCity, InterCity, Regional, etc.): ")
                filtered_trips = results.filterByTrainType(train_type_input, journeys)
                if not filtered_trips:
                    print("\nNo routes found with that filter.\n")
                else:
                    results.printJourneys(filtered_trips, limit=20)

            case 4:
                day_of_week_input = input("Enter the day of the week you wish to filter by (e.g., Mon, Tue, Wed, Thu, Fri, Sat, Sun): ")
                filtered_trips_day = results.filterByDayOfWeek(day_of_week_input, journeys)
                if not filtered_trips_day:
                    print("\nNo routes found with that filter.\n")
                else:
                    results.printJourneys(filtered_trips_day, limit=20)
            case _:
                print("Invalid entry. Returning back to the main menu...")
                return

        user_feedback_return = input("Do you wish to do another operation? 'y' for yes, 'n' for no (to exit the program): ")
        if (user_feedback_return.capitalize() in ["Y", "YES"]):
            askbooking()
        
    else:
        user_feedback_return = input("Do you wish to do another operation? 'y' for yes, 'n' for no (to exit the program): ")
        if (user_feedback_return.capitalize() in ["Y", "YES"]):
            askbooking() #the user might want to book, ask

def init_tables(con):
    users.init_users_table(con)
    connections.init_connections_table(con)
    reservations.init_reservations_table(con)
    trips.init_trips_table(con)
    tickets.init_tickets_table(con)

def main():
    con = sqlite3.connect("trainz.db")
    init_tables(con)

    choice = "Y"

    while choice.capitalize() in ["Y", "YES"]:
        printMenu()
        printTrips(con)
        choice = input("Would you like to continue?: ")

    print("\nThank you for using our Trainz: trip booking system!")
    con.close()

if __name__ == "__main__":
    main()