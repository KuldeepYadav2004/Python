class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    
    def print_details(self):
        print("Name:",self.name)
        print("Age:",self.age)


p1=Person('Vijay Verma',23)
p2=Person('Kuldeep Yadav',21)
p1.print_details()
p2.print_details()

