class Person:
    def set_details(self,name,age):
        self.name=name
        self.age=age
    def get_details(self):
        return 'name:' + self.name + '\nage:' + str(self.age)


p1=Person()
p2=Person()


p1.set_details(input('Enter name:'),int(input('Enter age:')))
p2.set_details(input('Enter name:'),int(input('Enter age:')))


print(p1.get_details())
print(p2.get_details())

