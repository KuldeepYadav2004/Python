def result(m1,m2,m3):
    t=m1+m2+m3
    p=t/300*100
    return t,p
m1=int(input('enter sub1 marks:'))
m2=int(input('enter sub2 marks:'))
m3=int(input('enter sub3 marks:'))
t,p=result(m1,m2,m3)
print('total of marks:',t)
print('percentage of marks:',p)
