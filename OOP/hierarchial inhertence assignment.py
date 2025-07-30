class Person:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
    def print_person_details(self):
        print("Name",self.name)
        print("Age",self.age)
        print("City",self.city)

class Students(Person):
    def __init__(self, roll_number,name,age,city,course,institute):
        #Person.__init__(self,name,age,city)
        super().__init__(name,age,city)
        self.roll_number=roll_number
        self.course=course
        self.institute=institute
    def print_student_details(self):
        print("Roll Number:",self.roll_number)
        print("Course:",self.course)
        print("Institute:",self.institute)


class Employee(Person):
    def __init__(self,employee_id, name, age, city,post,salary,company):
        super().__init__(name, age, city)
        self.employee_id=employee_id
        self.post=post
        self.salary=salary
        self.company=company
    def print_employee_details(self):
        print("Employee_id:",self.employee_id)
        print("Post:",self.post)
        print("Salary:",self.salary)
        print("company:",self.company)

s=Students(101,"Vijay verma",23,'Geater Noida',"Btech","abc engineering college")
s.print_person_details()
s.print_student_details()

e=Employee(1001,"manoj pandey",32,"new delhi","data anlyst",65000,"xyz infitech")

e.print_person_details()
e.print_employee_details()



        