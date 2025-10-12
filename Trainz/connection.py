class Connection:
    def __init__(self, route_id, departure, arrival, dep_time, arr_time,
                 train_type, days, first_class, second_class):
        self.route_id = route_id
        self.departure = departure
        self.arrival = arrival
        self.dep_time = dep_time
        self.arr_time = arr_time
        self.train_type = train_type
        self.days = days
        self.first_class = float(first_class)
        self.second_class = float(second_class)

    #to string
    def __str__(self): 
        return (
                    f"[{self.route_id}] {self.departure} → {self.arrival} | "
                    f"{self.train_type} | {self.days} | "
                    f"1st: €{self.first_class:.2f}, 2nd: €{self.second_class:.2f}"
                )
        '''
        self.route_id = arr[0].strip()
        self.dep_city = arr[1].strip()
        self.arr_city = arr[2].strip()
        self.dep_time = arr[3].strip()
        self.arr_time = arr[4].strip()
        self.train_type = arr[5].strip()
        self.op_days = self.determineOpDays(arr[6].strip())
        # convert rates to floats; if empty use 0.0
        try:
            self.fclass_rate = float(arr[7]) if arr[7] != "" else 0.0
        except ValueError:
            self.fclass_rate = 0.0

        try:
            self.sclass_rate = float(arr[8]) if arr[8] != "" else 0.0
        except ValueError:
            self.sclass_rate = 0.0
        '''
    
    def determineOpDays(self, str):
        days = {"Mon": False, 
                "Tue": False, 
                "Wed": False, 
                "Thu": False, 
                "Fri": False, 
                "Sat": False,
                "Sun": False}
        
        if str == "Daily":
            for key in days:
                days[key] = True

        elif str.find(',') != -1:
            for day in str.split(','):
                days[day] = True 

        elif str.find('-') != -1:
            foundVal = False
            for key in days:
                if key == str[0:3] or foundVal:
                    foundVal = True
                    days[key] = True

                if key == str[4:7]:
                    foundVal = False
                    
        return days    


'''
class Trip:
    def __init__(self, con1, con2 = None):
        self.con1 = con1
        self.con2 = con2
    
    def calculatePrice(self):
        return

'''