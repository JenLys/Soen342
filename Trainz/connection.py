class Connection:
    def __init__(self, route_id, departure, arrival, dep_time, arr_time,
                 train_type, days, first_class, second_class):
        self.route_id = route_id
        self.dep_city = departure
        self.arr_city = arrival
        self.dep_time = dep_time
        self.arr_time = arr_time
        self.train_type = train_type
        self.days = self.determineOpDays(days)
        self.fclass_rate = float(first_class)
        self.sclass_rate = float(second_class)

    #to string
    def __str__(self): 
        return (
                    f"[{self.route_id}] {self.dep_city} >> {self.arr_city} | "
                    f"{self.train_type} | {self.days} | "
                    f"1st: €{self.fclass_rate:.2f}, 2nd: €{self.sclass_rate:.2f}"
                )
    
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