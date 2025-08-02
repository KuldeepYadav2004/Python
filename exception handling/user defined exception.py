class InvalidAgeError(Exception):
    def __init__(self, message):
        Exception.__init__(self,message)

class Person:
    def __init__(self,value):
        if value >=0 and value <=100:
            self.age =value
        else:
            raise InvalidAgeError("Invalid age")
    def get_age(self):
        return self.age
try:
    p=Person(int(input("Enter your age:")))
except Exception as e:
    print(e)
else:
    print("Age:",p.get_age())
        