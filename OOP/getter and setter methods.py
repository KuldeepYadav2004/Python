class Person:
    def __init__(self,value1,value2):
        self.set_name(value1)
        self.set_age(value2)
    
    def get_age(self):
        return self.__age
    def get_name(self):
        return self.__name

    def set_name(self,value):
        self.__name=value
    def set_age(self,value):
        self.__age = value
    
    

p=Person("Vijay Verma",23)
print("Name:",p.get_name())
print("Age:",p.get_age())

        