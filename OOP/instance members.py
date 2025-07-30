class Person:
    def __init__(self,name,age,city):
        self.name = name
        self.age=age
        self.city=city
    def print_details(self):
        print('Name:',self.name)
        print('age:',self.age)
        print('city:',self.city)
    def update_city(self,new_city):
        self.city=new_city
        print('city is updated sucessfully')

p1=Person('Vijay Verma',23,'Greater Noida')
p2=Person('Mahima Gupta',22,'new delhi')
p1.print_details()
p2.print_details()
p1.update_city('banglore')
p1.print_details()
p2.print_details()





