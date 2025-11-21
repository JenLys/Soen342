import random
from trip import Trip
from reservation import Reservation
from ticket import Ticket 
import tickets #sql
import reservations
import trips

class BookingDBClass:

    trips_database = [] #all trips obj
    tickets_database = [] #all tickets stored obj

    def create_trip(user_id, reservations, current, con): #create a unique trip id, create trip and add to bookingdb's list
        #each trip has a unique trip_id, let's randomize it
        trip_id = "T"+ str(random.randint(0,99999))
        trip = Trip(trip_id,user_id, reservations, current)
        BookingDBClass.trips_database.append(trip)
        trips.insert_trip(trip, con)
        return trip #trip object with unique id

    def create_ticket(user_id, reservation_id, ticket_id, con): #preconditions are that there's a user and a reservation id
        ticket = Ticket(user_id,reservation_id, ticket_id)
        BookingDBClass.tickets_database.append(ticket)
        #persistance
        tickets.insert_ticket(ticket, con)

        print(f"Ticket {ticket_id} created")
        #tickets.show_all_tickets() #SELECT * from the table of tickets
        return ticket

    def create_reservation(fname,lname,age,selected_option, user_id, con):
        #create the reservation object
        reservation = Reservation(fname,lname,age,selected_option)
        #this line is to insert the reservation into the sql table
        reservations.insert_reservation(reservation, con)
        
        # a ticket gets created and stored in memory
        ticket_id = "ticket-"+str(random.randint(0,99999))

        # a ticket gets created and stored in memory

        ticket=BookingDBClass.create_ticket(user_id,reservation.reservation_id, ticket_id, con)
        return reservation
    
    def view_past(lname, user_id, con):
        past_trips = trips.find_past_trips(user_id, con)
        if len(past_trips) == 0:
            print("No past trips found for given user")
        else:
            for trip in past_trips:
                print(trip)

    def view_current(lname, user_id, con):
        current_trips = trips.find_current_trips(user_id, con)
        if len(current_trips) == 0:
            print("No current trips found for given user")
        else:
            for trip in current_trips:
                print(trip)

    def view_trips(lname, user_id, con):
        BookingDBClass.view_past(lname, user_id, con)
        BookingDBClass.view_current(lname, user_id, con)