import trip
import random
from trip import TripContainer

class BookingDBClass:

    def create_trip():
        #each trip has a unique trip_id, let's randomize it
        trip_id = "T"+ random.randint(0,99999)
        trip(trip_id)

        pass

    def create_reservation(fname,lname,age,selected_option, user_id):
        pass
        #create the trip object that will store the session's reservations
        #upon creation the trip receives its uniqueid----this will be done in trip.py

        #create the reservation object

        #store the reservation object in the newly created trip container


    def create_ticket():
        pass