class Person:
    def input_details(p):
        p.name=input('Enter name:')
        p.age=int(input('enter age:'))

    def print_details(p):
        print('Name:',p.name)
        print('age:',p.age)



p1=Person()
p2=Person()

Person.input_details(p1)
Person.input_details(p2)

Person.print_details(p1)
Person.print_details(p2)



        
        
