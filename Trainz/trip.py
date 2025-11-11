class TripContainer: #a trip is a container of reservations. each time you do a booking, you create a Trip "container"
    

    def __init__(self, trip_id, user_id): #a trip is like a shopping cart to a user, it should link back to them for better lookup
        self.trip_id = trip_id
        self.user_id = [user_id] # changed to list so all users on this trip (if family) can access the trip with their own id
        self.reservation_list = [] #trip is a container containing the user's reservations--- list
    
    def add_reservation(self, reservation):
        self.reservation_list.append(reservation)
        print("Reservation added to trip container. remove this print after testing")

    # adding user to trip list so that all users on this trip can access the trip with their id
    def add_trip_member(self, user_id):
        self.user_id.append(user_id)