class Person:
    def __init__(self,value):
        self.age=value
    def print_age(self):
        print("Age:",self.age)

p=Person(23)
p.print_age()
print("Age:",p.age)
p.age=-45
p.print_age()

        