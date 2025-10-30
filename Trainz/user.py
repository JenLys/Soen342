class User:
    #default constructor + getters and setters

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

    def getName(self):
        return f"{self.fname} {self.lname}"
    
    def getAge(self):
        return self.age
    
    def getId(self):
        return self.user_id