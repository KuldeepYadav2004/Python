class Person:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city

    def print_person_details(self):
        print("Name:",self.name)
        print("age:",self.age)
        print("city:",self.city)


class Students:
    def __init__(self,roll_number,name,age,city,course,institute):
        self.roll_number=roll_number
        self.name=name
        self.age=age
        self.city=city
        self.course=course
        self.institute=institute

    def print_student_details(self):
        print("Roll number:",self.roll_number)
        print("Name:",self.name)
        print("age:",self.age)
        print("city:",self.city)
        print('course:',self.course)


        
    
        