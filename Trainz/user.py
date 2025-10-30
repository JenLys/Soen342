class User:
    #default constructor + getters and setters

    def __init__(self, lname, fname, user_id, age ):
        self.lname = lname
        self.fname = fname
        self.user_id = user_id
        self.age = age

    def getName():
        return f"{self.fname} {self.lname}"
    
    def getAge():
        return self.age
    
    def getId():
        return self.user_id