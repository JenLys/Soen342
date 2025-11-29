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
indexIDs = [] #saving the ids and trips.journey(actual connections) pair
currentIndex = 1 #ids increase persists post search to book trips.journey, user dont see the actual trip ids

# TODO check printTrips and viewBooking
def printTrips(con):
    choice = input("Would you like to see Trips for a given user (must be the booking user)?: ")

    if choice.capitalize() not in ["Y", "YES"]:
        return
    
    user_id = input("Please enter your User ID: ")

    while users.find_user(user_id, con) == None:
        print("User could not be found... Please try again")
        user_id = input("User ID: ")

    print("Which trips would you like to see?")
    print("1. Past")
    print("2. Current")
    print("3. All")
    choice = int(input("Choice: "))

    match choice:
        case 1:
            BookingDBClass.view_past(user_id, con)
        case 2:
            BookingDBClass.view_current(user_id, con)
        case 3:
            BookingDBClass.view_trips(user_id, con)
        case _:
            print("Incorrect input, returning to main menu...")

def viewBooking():
    pass


#Function called when the user desires to make a booking (reservation of a displayed result)
def askbooking(con):
    global indexIDs
    global currentIndex
    booking_req_input = input("Do you wish to do a booking? 'y' for yes, 'n' for no: ")
    if (booking_req_input.capitalize() in ["Y", "YES"]):
        bookNow = input("Do you wish to book for now (current)? select y-yes or n-no if you wish to book for later: ")
        if bookNow.capitalize() in ["Y", "YES"]:
            current = True #the booked selection is for a CURRENT TRIP
        else:
            current = False # PAST TRIP


        if current:
            #a person can book for themselves, or do multiple bookings (each reservation under the other name)
            num = int(input("How many people will be booking today?: "))
            print("/n")

            main_user_id = 0
            reservation_list = ""
            
            for index in range(num): #loop for each person
                while True:
                    user_id = input("Please enter your user ID: ")

                    user = users.find_user(user_id, con)

                    fname = None
                    lname = None
                    age = None

                    if user != None:
                        fname = user.fname
                        lname = user.lname
                        age = user.age
                    
                    if user == None:
                        booking_user_info = input("Please identify yourself to proceed with the booking: first name, last name, age: ")
                        #in case the user enters gibberish, try catch
                        try:
                            fields = booking_user_info.split(",") #extracts fields split by ,
                            #extra info added, reject
                            if len(fields) != 3:
                                raise ValueError("The system was not able to identify you. Please try again \n")
                            
                            fname, lname, age = fields #assigned in order
                            fname = fname.strip()
                            lname = lname.strip()
                            age = age.strip()
                            #validate type (positive age only, can add more filters later)
                            age = int(age)
                            while age < 0:
                                age = int(input("You have entered an invalid age. Please try again: "))

                            user = User(fname, lname, user_id, age) #creates a new user and stores it in the user database
                            users.insert_user(user, con)

                            print("User identified, proceed to do booking...")

                        except ValueError as e:
                            print("The system was not able to identify you. Please try again")
                            continue

                    selected_option = int(input("Which option would you like to book? Please enter the result's id: ")) #corresponds to result_id
                    # get the number
                    for tr in indexIDs:
                            if int(tr["tempID"]) == selected_option:
                                actualSelect = tr["trip"].tripID
                    reservation = BookingDBClass.create_reservation(fname,lname,age,actualSelect,user_id,con)

                    if index == 0:
                        main_user_id = user_id
                        reservation_list = reservation.reservation_id
                    else:
                        reservation_list = reservation_list +  ", " + reservation.reservation_id
                    break

            BookingDBClass.create_trip(actualSelect, main_user_id, reservation_list, current, con)
    #user doesn't select Yes --replies No or something else
    else: 
        print("Returning to Trainz System... \n")

def displayConnectionsByParameter(connections: List[connection.Connection]):
    global indexIDs
    global currentIndex
    print("1: Departure City")
    print("2: Arrival City")
    print("3: Departure Time and Date")
    print("4: Arrival Time and Date")
    print("5: Days of Operation")
    print("6: Train Type")
    print("7: First class ticket rate (Euros)")
    print("8: Second class ticket rate (Euros)")

    parameter = int(input("Choice (1-7): "))

    if(parameter == 3 or parameter == 4):
        print("(Enter as [Time, Date])")

    value = input("Please enter a value: ")

    match parameter:
        case 1: # by departure
            for connection in connections:
                if connection.dep_city.capitalize() == value.capitalize():
# #TODO this below block really should be refactored into a function, but whatever
                    indexIDs.append({"tempID" : currentIndex, "trip": connection})
                    print(f"[Trip index {currentIndex}] {connection}")
                    currentIndex += 1
# end of block
        case 2: # by arrival
            for connection in connections:
                if connection.arr_city.capitalize() == value.capitalize():
                    indexIDs.append({"tempID" : currentIndex, "trip": connection})
                    print(f"[Trip index {currentIndex}] {connection}")
                    currentIndex += 1

        case 3: # by departure time
            value = value.split(", ")
            for connection in connections:
                if connection.dep_time == value[0] and connection.days[value[1]]:
                    indexIDs.append({"tempID" : currentIndex, "trip": connection})
                    print(f"[Trip index {currentIndex}] {connection}")
                    currentIndex += 1

        case 4: # by arrival time
            value = value.split(", ")
            for connection in connections:
                if connection.arr_time == value[0] and connection.days[value[1]]:
                    indexIDs.append({"tempID" : currentIndex, "trip": connection})
                    print(f"[Trip index {currentIndex}] {connection}")
                    currentIndex += 1

        case 5: # day of week
            for connection in connections:
                if value.capitalize() == connection.days_str.capitalize():
                    indexIDs.append({"tempID" : currentIndex, "trip": connection})
                    print(f"[Trip index {currentIndex}] {connection}")
                    currentIndex += 1

        case 6: # train type
            for connection in connections:
                if value.capitalize() == connection.train_type.capitalize():
                    indexIDs.append({"tempID" : currentIndex, "trip": connection})
                    print(f"[Trip index {currentIndex}] {connection}")
                    currentIndex += 1

        case 7: # first class ticket price
            for connection in connections:
                if connection.fclass_rate == int(value):
                    indexIDs.append({"tempID" : currentIndex, "trip": connection})
                    print(f"[Trip index {currentIndex}] {connection}")
                    currentIndex += 1

        case 8: # second class ticket price
            for connection in connections:
                if connection.sclass_rate == int(value):
                    indexIDs.append({"tempID" : currentIndex, "trip": connection})
                    print(f"[Trip index {currentIndex}] {connection}")
                    currentIndex += 1

def searchConnections(db: RecordsDB, con):
    choice = "Y"

    while(choice.capitalize() in ["YES", "Y"]):
        connections = db.getAllConnections()
        print("Which parameter would you like to search by?")
        displayConnectionsByParameter(connections)
        choice = input("Would you like to make another search? y for yes, anything else to skip: ")

    # done looking for trips now book
    askbooking(con)
        
#NOTE: at the very end, once all is done we can refactor code and make the Interface code cleaner- while loop instead of ifs
def printMenu(db: RecordsDB, con):
    global currentIndex
    global indexIDs

    dep_station = input("Where are you departing from? (enter initial station name): ")
    arr_station = input("What is your destination? (enter final station name): ")

    # input sanitizing
    dep_station = dep_station.strip().capitalize()
    arr_station = arr_station.strip().capitalize()

    journeys = results.searchForConnections(db, dep_station, arr_station, max_depth=3)
    #call search method
    if not journeys:
        print("\nNo routes found between those cities.\n")
    else:
        print(f"\nFound {len(journeys)} possible journey(s):\n")
        # need to persist, changing
        for t in journeys:
            indexIDs.append({"tempID" : currentIndex, "trip": t})
            print(f"[Trip index {currentIndex}] {t}")
            currentIndex += 1

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
# TODO refactor this block
# ###bad practice here, fix later (all the temp sorted double for-loops)
                tempSorted = results.sortByDuration(journeys)
                for sorted in tempSorted:
                    for globalTrips in indexIDs:
                        if globalTrips["trip"].tripID == sorted.tripID:
                            print(f"[Trip index {globalTrips["tempID"]}] {globalTrips["trip"]}")
                        continue
# bad block end
                
            case 2:
                print("Results sorted from lowest to highest price: \n")
                tempSorted = results.sortByPrice(journeys)
                for sorted in tempSorted:
                    for globalTrips in indexIDs:
                        if globalTrips["trip"].tripID == sorted.tripID:
                            print(f"[Trip index {globalTrips["tempID"]}] {globalTrips["trip"]}")
                        continue

            case 3:
                train_type_input = input("Enter the train type you wish to filter by (e.g., EuroCity, InterCity, Regional, etc.): ")
                filtered_trips = results.filterByTrainType(train_type_input, journeys)
                if not filtered_trips:
                    print("\nNo routes found with that filter.\n")
                else:
                    for filtered in filtered_trips:
                        for globalTrips in indexIDs:
                            if globalTrips["trip"].tripID == filtered.tripID:
                                print(f"[Trip index {globalTrips["tempID"]}] {globalTrips["trip"]}")
                            continue

            case 4:
                day_of_week_input = input("Enter the day of the week you wish to filter by (e.g., Mon, Tue, Wed, Thu, Fri, Sat, Sun): ")
                filtered_trips_day = results.filterByDayOfWeek(day_of_week_input, journeys)
                if not filtered_trips_day:
                    print("\nNo routes found with that filter.\n")
                else:
                    for filtered in filtered_trips:
                        for globalTrips in indexIDs:
                            if globalTrips["trip"].tripID == filtered.tripID:
                                print(f"[Trip index {globalTrips["tempID"]}] {globalTrips["trip"]}")
                            continue

            case _:
                print("Invalid entry. Continuing...")

        # ok you sorted, now do you want to book?
        askbooking(con)
        
    else:
        # dont want to sort, but do you want to book?
        askbooking(con) #the user might want to book, ask

def init_tables(con):
    users.init_users_table(con)
    connections.init_connections_table(con)
    reservations.init_reservations_table(con)
    trips.init_trips_table(con)
    tickets.init_tickets_table(con)

def main():
    con = sqlite3.connect("trainz.db")
    init_tables(con)

    users.show_all_users(con)
    reservations.show_all_reservations(con)
    trips.show_all_trips(con)
    tickets.show_all_tickets(con)

    #call on to load csv data
    db = RecordsDB(file)

    while True:
        # changing to pre-choices
        print("\n\nPlease choose an option from below:")
        print("1. Find trips by entering departure and arrival")
        print("2. Find trips by other parameters")
        print("3. View bookings")
        print("4. Exit program")
        choice = input("Please enter number: ")

        choice = choice.strip()

        match choice:
            case '1':
                printMenu(db, con)
            case '2':
                searchConnections(db, con)
            case '3':
                viewBooking()
            case '4':
                print("Thank you for using Trainz System")
                con.close()
                sys.exit(0)
            case _:
                print("Invalid input, please select again")

    '''
    users.show_all_users(con)
    reservations.show_all_reservations(con)
    trips.show_all_trips(con)
    tickets.show_all_tickets(con)
    '''


if __name__ == "__main__":
    main()