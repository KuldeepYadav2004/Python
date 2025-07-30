class Person:
    pass
p1=Person()
p2=p1

print(id(p1))
print(id(p2))



p1.name='vijay verma'
p1.age=23


print('name:',p2.name)
print('age:',p2.age)

print('name:',p1.name)
print('age:',p1.age)



