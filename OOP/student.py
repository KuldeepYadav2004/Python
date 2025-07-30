class Student:
    def input_detail(s):
        s.roll_number=input('Enter Roll number:')
        s.Name=input('Name:')
        s.m1=int(input('Enter of marks of sub 1:'))
        s.m2=int(input('Enter of marks of sub 2:'))
        s.m3=int(input('Enter of marks of sub 3:'))


    def find_result(r):
        r.total=r.m1 + r.m2+r.m3
        r.percentage=r.total/300*100

    def print_result(p):
        print('Roll Number:',p.roll_number)
        print('Name:',p.Name)
        print('m1:',p.m1)
        print('m2:',p.m2)
        print('m3:',p.m3)
        print('Total of marks:',p.total)
        print('Percentage of marks:',round(p.percentage,2))



x=Student()
Student.input_detail(x)
Student.find_result(x)
Student.print_result(x)













        
