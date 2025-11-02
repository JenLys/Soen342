import random

class ReservationClass:
    def __init__(self, fname, lname, selected): #selected is the selected option to book
        #each reservation has a unique reservation id
        self.reservation_id = "R"+random.randint(0,99999)
        self.fname = fname
        self.lname = lname
        self.selected = selected

