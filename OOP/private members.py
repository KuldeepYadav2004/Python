class Person:
    def __init__(self,value):
        self.__age = value
    def print_age(self):
        print("Age:",self.__age)
    
p=Person(23)
p.print_age()
print("Age:",p.__age)

    