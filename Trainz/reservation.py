import random

class ReservationClass:
    def __init__(self, fname, lname,age, selected_option): #*selected option to book
        #each reservation has a unique reservation id
        self.reservation_id = "R"+str(random.randint(0,99999))
        self.fname = fname
        self.lname = lname
        self.age = age
        self.selected = selected_option


