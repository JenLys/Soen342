import trip
import random
from trip import TripContainer
from reservation import ReservationClass
from ticket import Ticket 
import tickets #sql
import datetime

class BookingDBClass:

    trips_database = [] #all trips obj
    tickets_database = [] #all tickets stored obj

    def create_trip(user_id): #create a unique trip id, create trip and add to bookingdb's list
        #each trip has a unique trip_id, let's randomize it
        # why randomize it???
        trip_id = "T"+ str(random.randint(0,99999))
        trip = TripContainer(trip_id,user_id)
        BookingDBClass.trips_database.append(trip)
        return trip #trip object with unique id

    def create_ticket(user_id, reservation_id, ticket_id): #preconditions are that there's a user and a reservation id
        ticket = Ticket(user_id,reservation_id, ticket_id)
        BookingDBClass.tickets_database.append(ticket)
        #persistance
        tickets.insert_ticket(ticket_id, user_id, reservation_id)

        print(f"Ticket {ticket_id} created")
        #tickets.show_all_tickets() #SELECT * from the table of tickets
        return ticket

    def create_reservation(fname,lname,age,selected_option, user_id, date, current):
        #create the trip object that will store the session's reservations
        trip = BookingDBClass.create_trip(user_id)
        #create the reservation object
        reservation = ReservationClass(fname,lname,age,selected_option, date, current)
        #store the reservation object in the newly created trip container
        trip.add_reservation(reservation)
        print("Trip container contains the reservation")
        
        # a ticket gets created and stored in memory
        ticket_id = "ticket-"+str(random.randint(0,99999))

        # a ticket gets created and stored in memory

        ticket=BookingDBClass.create_ticket(user_id,reservation.reservation_id, ticket_id)

        # need the reference to append to the trip
        return trip.trip_id
    
    # should always work, to get the trip from id
    def find_trip(trip_id):
        for t in BookingDBClass.trips_database:
            if t.trip_id == trip_id:
                return t

    # adding more members to an already created trip
    def append_reservation(tripId, fname,lname,age,selected_option, user_id, date, current):
        #create the trip object that will store the session's reservations
        trip = BookingDBClass.find_trip(tripId)
        #get the reservation object
        reservation = ReservationClass(fname,lname,age,selected_option, date, current)
        #store the reservation object in the newly created trip container
        trip.add_reservation(reservation)
        print("Trip container contains the reservation")
        trip.add_trip_member(user_id)
        
        # a ticket gets created and stored in memory
        ticket_id = "ticket-"+str(random.randint(0,99999))

        # a ticket gets created and stored in memory

        ticket=BookingDBClass.create_ticket(user_id,reservation.reservation_id, ticket_id)

    # user enters lname and id, but only use id
    def getReservationsFromUserId(userId):
        tempAllTrips = []
        tempAllTicketsResId = []
        # get all trips of user, userId is a list
        for trip in BookingDBClass.trips_database:
            if userId in trip.user_id:
                tempAllTrips.append(trip)

        # user has no trips, abort
        if not tempAllTrips:
            return []
        
        # find tickets of user for reservation ids
        for ticket in BookingDBClass.tickets_database:
            if userId == ticket.user_id:
                tempAllTicketsResId.append(ticket.reservation_id)

        # get today's date to sort trips in past/current
        date = str(datetime.datetime.now())
        date = date.split()[0].split('-')
        year = int(date[0])
        month = int(date[1])
        day = int(date[2])
        userPast = []
        userCurrent = []
        
        for tr in tempAllTrips:
            # get reservation container in trips
            for res in tr.reservation_list:
                # get reservation from reservation id
                if res.reservation_id in tempAllTicketsResId:
                    # get reservation date and check
                    isPast = False
                    rd = res.date.split("-")
                    ryear = rd[0]
                    rmonth = rd[1]
                    rday = rd[2]
                    # if previous year
                    if ryear < year:
                        isPast = True
                    # previous month of this year
                    elif ryear == year and rmonth < month:
                        isPast = True
                    # previous day of this month
                    elif rmonth == month and rday < day:
                        isPast = True
                    
                    if isPast:
                        userPast.append(res)
                    else:
                        userCurrent.append(res)

        userReservationsOut = [userPast, userCurrent]
        return userReservationsOut


