class Student:
    def input_detail(self):
        self.roll_number=input('Enter Roll number:')
        self.Name=input('Name:')
        self.m1=int(input('Enter of marks of sub 1:'))
        self.m2=int(input('Enter of marks of sub 2:'))
        self.m3=int(input('Enter of marks of sub 3:'))


    def find_result(self):
        self.total=self.m1 + self.m2+self.m3
        self.percentage=self.total/300*100

    def print_result(self):
        print('Roll Number:',self.roll_number)
        print('Name:',self.Name)
        print('m1:',self.m1)
        print('m2:',self.m2)
        print('m3:',self.m3)
        print('Total of marks:',self.total)
        print('Percentage of marks:',round(self.percentage,2))



s1=Student()
s1.input_detail()
s1.find_result()
s1.print_result()













        
