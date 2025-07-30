class Person:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city

    def print_person_details(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("City:",self.city)

class Student(Person):
    def __init__(self, roll_number,name, age, city,course,institute):
        Person.__init__(self,name,age,city)
        self.roll_number=roll_number
        self.course=course
        self.institute=institute

    def print_student_details(self):
        print("Roll Number:",self.roll_number)
        print("course:",self.course)
        print("Institute:",self.institute)

class Result(Student):
    def __init__(self, roll_number, name, age, city, course, institute,marks1,marks2,marks3):
        Student.__init__(self,roll_number,name,age,city,course,institute)
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
    def print_result_details(self):
        total=self.marks1+self.marks2+self.marks3
        percentage= total/300*100
        print("Marks of first subject:",self.marks1)
        print("Marks of second subject:",self.marks2)
        print("Marks of third subject:",self.marks3)
        print("Total of marks:",total)
        print("Percentage of Marks:",round(percentage,2))

r=Result(101,"Vijay Verma",23,"Noida","Btech","xyz eng",45,39,56)
r.print_person_details()
r.print_student_details()
r.print_result_details()







        
        