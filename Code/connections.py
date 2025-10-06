class Connection:
    def __init__(self, arr):
        self.route_id = arr[0]
        self.dep_city = arr[1]
        self.arr_city = arr[2]
        self.dep_time = arr[3]
        self.arr_time = arr[4]
        self.train_type = arr[5]
        self.op_days = determineOpDays(arr[6])
        self.fclass_rate = arr[7]
        self.sclass_rate = arr[8]
    
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

        elif str.find('\"') != -1:
            new_str = str[1:len(str) - 1]
            for day in new_str.split(','):
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