class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    
    def print_details(self):
        return "Name :" + self.name + "\nAge:  "  + str(self.age)


p1=Person(input('enter the name:'),int(input('enter the age:')))
p2=Person(input('enter the name:'),int(input('enter the age:')))
print(p1.print_details())
print(p2.print_details())

