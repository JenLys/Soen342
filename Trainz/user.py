class User:
    #default constructor + getters and setters
    user_list = [] #database of all registered users

    def __init__(self, lname, fname, user_id, age ):
        self.lname = lname
        self.fname = fname
        self.user_id = user_id
        #age is an integer
        try:
            age=int(age)
            if age <=0: #already checking in main.py, this is a double precaution
                raise ValueError("Invalid age")
            self.age = age
        except ValueError:
            raise ValueError("Invalid Age")
        #passes verifications-- can add to user list/ store in database
        User.user_list.append(self)

    def getName(self):
        return f"{self.fname} {self.lname}"
    
    def getAge(self):
        return self.age
    
    def getId(self):
        return self.user_id
    
    def __str__(self):
        return f"user_id: {self.user_id}, lname: {self.lname}, fname: {self.fname}, age: {self.age}"