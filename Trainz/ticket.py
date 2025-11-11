#contract between a user and the reservation-- proof of booking
#association class
class Ticket:
    def __init__(self, user_id, reservation_id, ticket_id):
        self.user_id = user_id
        self.reservation_id = reservation_id
        self.ticket_id = ticket_id


    def getTicketId(self):
        return self.ticket_id
