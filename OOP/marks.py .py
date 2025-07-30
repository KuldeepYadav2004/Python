class marks:
    pass


m=marks()

m.s1=int(input('enter sub1 marks:'))
m.s2=int(input('enter sub2 marks:'))
m.s3=int(input('enter sub3 marks:'))
m.sum=m.s1+m.s2+m.s3

print('total marks:',sum)
m.p=m.sum/300*100


print('percentage:',m.p)

