class Student:
    def __init__(self):
        self.roll_number=int(input('Enter roll number:'))
        self.name=input('Enter name:')
        self.marks1=int(input('enter marks of first subject:'))
        self.marks2=int(input('enter marks of second subject:'))
        self.marks3=int(input('enter marks of third subject:'))
    
    def find_total_percentage(self):
        self.total=self.marks1+self.marks2+self.marks3
        self.percentage=self.total/300*100
   
    def print_details(self):
        print('Roll number:',self.roll_number)
        print('name:',self.name)
        print('marks1:',self.marks1)
        print('marks2:',self.marks2)
        print('marks3:',self.marks3)
        print('total of marks:',self.total)
        print('percentage of marks :',self.percentage)


s=Student()
s.find_total_percentage()
s.print_details()

