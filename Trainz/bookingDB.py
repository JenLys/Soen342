import trip
import random
from trip import TripContainer
from reservation import ReservationClass
from ticket import Ticket 

class BookingDBClass:

    trips_database = [] #all trips
    tickets_database = [] #all tickets stored

    def create_trip(user_id): #create a unique trip id, create trip and add to bookingdb's list
        #each trip has a unique trip_id, let's randomize it
        trip_id = "T"+ str(random.randint(0,99999))
        trip = TripContainer(trip_id,user_id)
        BookingDBClass.trips_database.append(trip)
        return trip #trip object with unique id

    def create_ticket(user_id, reservation_id, ticket_id): #preconditions are that there's a user and a reservation id
        ticket = Ticket(user_id,reservation_id, ticket_id)
        BookingDBClass.tickets_database.append(ticket)
        print("Ticket created")

    def create_reservation(fname,lname,age,selected_option, user_id):
        pass
        #create the trip object that will store the session's reservations
        trip = BookingDBClass.create_trip(user_id)
        #create the reservation object
        reservation = ReservationClass(fname,lname,age,selected_option)
        #store the reservation object in the newly created trip container
        trip.add_reservation(reservation)
        print("Trip container contains the reservation")
        
        # a ticket gets created and stored in memory
        ticket_id = "ticket-"+str(random.randint(0,99999))

        # a ticket gets created and stored in memory

        ticket=BookingDBClass.create_ticket(user_id,reservation.reservation_id, ticket_id)

