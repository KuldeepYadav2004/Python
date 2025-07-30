age=int(input('enter your age:'))

if age>=0 and age <=100:
    if age >=18:
        print('you can vote')
    else:
        print("you can't vote")
    
else:
    print('Invalid age')
