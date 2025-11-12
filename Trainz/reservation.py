import random

class ReservationClass:
    def __init__(self, fname, lname,age, selected_option, date, current): #*selected option to book
        #each reservation has a unique reservation id
        self.reservation_id = "R"+str(random.randint(0,99999))
        self.fname = fname
        self.lname = lname
        self.age = age
        self.selected = selected_option
        self.date = date
        self.current = True #by default set for "book for now-- current trip"

    def __str__(self):
        return (
            f"Booking of {self.fname} {self.lname}, age {self.age}"
            f"\nTrip {self.selected} at date: {self.date}"
        )
