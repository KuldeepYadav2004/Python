class Person:
    def __init__(self):
        self.name=input("Enter name:")
        self.age=int(input("Enter age:"))

    
    def print_details(self):
        print("Name:",self.name)
        print("Age:",self.age)


p1=Person()
p2=Person()
p1.print_details()
p2.print_details()

