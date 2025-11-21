class Trip: #a trip is a container of reservations. each time you do a booking, you create a Trip "container"
    def __init__(self, trip_id, user_id, reservation_list, current = True): #a trip is like a shopping cart to a user, it should link back to them for better lookup
        self.trip_id = trip_id
        self.user_id = user_id
        self.reservation_list = reservation_list #trip is a container containing the user's reservations (ids)--- list
        self.current = current #by default set for "book for now-- current trip"

    def add_reservation(self, reservation):
        if len(self.reservation_list):
            self.reservation_list = reservation.reservation_id + ""
            return
        self.reservation_list = ", " + self.reservation_list + reservation.reservation_id

    def __str__(self):
        state = "False" if self.current else "True"
        return (
            f"Trip ID: {self.trip_id}, "
            f"User ID: {self.user_id}, "
            f"Reservation List: {self.reservation_list}, "
            f"Finished: {state}, "
        )

