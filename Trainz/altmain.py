import glob
import time
import sys
from typing import List
from user import User
import connection, os
import results
from reservation import ReservationClass
from bookingDB import BookingDBClass
import recordDB
from recordDB import RecordsDB #import the class

# cleaning up the main function
# further refactoring from today
# sorry yall are losing work

dir = os.path.dirname(__file__)
file = dir + "/eu_rail_network.csv"
indexIDs = [] #saving the ids and trips(actual connections) pair
currentIndex = 1 #ids increase persists post search to book trips, user dont see the actual trip ids

#Function called when the user desires to make a booking (reservation of a displayed result)
def askbooking():
    global indexIDs
    global currentIndex
    booking_req_input = input("Do you wish to do a booking? 'y' for yes, 'n' for no: ")
    if (booking_req_input.lower() == "y" or booking_req_input.lower() == "yes"):
        bookNow = input("Do you wish to book for now (current)? select y-yes or enter anything if you wish to see bookings: ")

        if bookNow.lower() == "y" or bookNow.lower() == "yes":
            current = True #the booked selection is for a CURRENT TRIP
        else:
            current = False # PAST TRIP
            # but you cant book past trips???
            # what is the point??????

        # trip booking
        if current:
            #a person can book for themselves, or do multiple bookings (each reservation under the other name)
            num = int(input("How many people will be booking today?: "))
            print("/n")
            
            
            for _ in range(num): #loop for each person
                #user provides user info in order to book (name, id, age, ...)
                while True:
                    booking_user_info = input("Please identify yourself to proceed with the booking: first name,last name,age,id  (*commas included with no space): ")
                    #in case the user enters gibberish, try catch
                    try:
                        fields = booking_user_info.split(",") #extracts fields split by ,
                        #extra info added, reject
                        if len(fields) != 4:
                            raise ValueError("The system was not able to identify you. Please try again \n")
                            
                        
                        fname, lname, age, user_id = fields #assigned in order
                        #validate type (positive age only, can add more filters later)
                        age_input = int(age)
                        if age_input <= 0:
                            raise ValueError("You have entered an invalid age. Try again...\n")
                        user = User(fname,lname,user_id,age) #creates a new user and stores it in the user database
                        print("User identified, proceed to do booking...")    

                        selected_option = int(input("Which option would you like to book? Please enter the result's id: ")) #corresponds to result_id
                        for tr in indexIDs:
                            if int(tr["tempID"]) == selected_option:
                                actualSelect = tr["trip"].tripID
                        date = input("please also add the date for when you are booking in the form of aaaa-mm-dd: ") #currently not checked
                        BookingDBClass.create_reservation(fname,lname,age,actualSelect, user_id, date, current)

                        break 

                    except ValueError as e:
                        print("The system was not able to identify you. Please try again")

        # current/history view
        else:
            nolname = input("Please enter your last name: ")
            id = input("Please enter your id: ")
            pastpres = input("Enter 1 for current trips or 2 for past trips: ")
            print("\nResults:")
            pastpres = str(pastpres).strip()
            match pastpres:
                case '1':
                    output = BookingDBClass.getReservationsFromUserId(id, pastpres)
                    if type(output)=='str':
                        print(output)
                    else:
                        for o in output:
                            print(o)
                case '2':
                    output = BookingDBClass.getReservationsFromUserId(id, pastpres)
                    if type(output)=='str':
                        print(output)
                    else:
                        for o in output:
                            print(o)
                case _:
                    print("Invalid choice, leaving...")
   
#user doesn't select Yes --replies No or something else
    else: 
        # it's already redirecting choices from the match case
        pass

def viewBooking():
    nolname = input("Please enter your last name: ")
    id = input("Please enter your id: ")
    pastpres = input("Enter 1 for current trips or 2 for past trips: ")
    print("\nResults:")
    pastpres = str(pastpres).strip()
    match pastpres:
        case '1':
            output = BookingDBClass.getReservationsFromUserId(id, pastpres)
            if type(output)=='str':
                print(output)
            else:
                for o in output:
                    print(o)
        case '2':
            output = BookingDBClass.getReservationsFromUserId(id, pastpres)
            if type(output)=='str':
                print(output)
            else:
                for o in output:
                    print(o)
        case _:
            print("Invalid choice, leaving...")

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
# this below block really should be refactored into a function, but whatever
                    indexIDs.append({"tempID" : currentIndex, "trip": connection})
                    print(f"[Trip index {currentIndex}] {connection}")
                    currentIndex += 1

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

def searchConnections(db: RecordsDB):

    choice = 'Y'

    print("Which parameter would you like to search by?")
    while(choice.capitalize() in ["YES", "Y"]):
        connections = db.getAllConnections()
        displayConnectionsByParameter(connections)
        choice = input("Would you like to make another search? y for yes, anything else to skip: ")

    # done looking for trips now book
    askbooking()
        
#NOTE: at the very end, once all is done we can refactor code and make the Interface code cleaner- while loop instead of ifs
def tripsByDepartsArrives(db: RecordsDB): 
    global currentIndex
    global indexIDs

    dep_station = input("Where are you departing from? (enter initial station name): ")
    arr_station = input("What is your destination? (enter final station name): ")
    
    # input sanitizing
    dep_station = dep_station.strip().capitalize()
    arr_station = arr_station.strip().capitalize()

    # search for trips (returns list of Trip objects)
    trips = results.searchForConnections(db, dep_station, arr_station, max_depth=3)
    #call search method
    if not trips:
        print("\nNo routes found between those cities.\n")
    else:
        print(f"\nFound {len(trips)} possible trip(s):\n")
        # results.printTrips(trips, limit=20)  # limit to first 20 for readability
        # need to persist, changing
        for t in trips:
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
# ###bad practice here, fix later (all the temp sorted double for loops)
                tempSorted = results.sortByDuration(trips)
                for sorted in tempSorted:
                    for globalTrips in indexIDs:
                        if globalTrips["trip"].tripID == sorted.tripID:
                            print(f"[Trip index {globalTrips["tempID"]}] {globalTrips["trip"]}")
                        continue
                    # if sorted. compared 2 ids but need to make new trip id first
                
            case 2:
                print("Results sorted from lowest to highest price: \n")
                tempSorted = results.sortByPrice(trips)
                for sorted in tempSorted:
                    for globalTrips in indexIDs:
                        if globalTrips["trip"].tripID == sorted.tripID:
                            print(f"[Trip index {globalTrips["tempID"]}] {globalTrips["trip"]}")
                        continue

            case 3:
                train_type_input = input("Enter the train type you wish to filter by (e.g., EuroCity, InterCity, Regional, etc.): ")
                filtered_trips = results.filterByTrainType(train_type_input, trips)
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
                filtered_trips_day = results.filterByDayOfWeek(day_of_week_input, trips)
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
        askbooking()
        
    else:
        # dont want to sort, but do you want to book?
        askbooking() #the user might want to book, ask

def main():
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
                #call method to print menu
                tripsByDepartsArrives(db)
            case '2':
                searchConnections(db)
            case '3':
                viewBooking()
            case '4':
                print("Thank you for using Trainz System")
                sys.exit(0)
            case _:
                print("Invalid input, please select again")

if __name__ == "__main__":
    main()