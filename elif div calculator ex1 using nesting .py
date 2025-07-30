m1=float(input('enter the 1st sub marks:'))
m2=float(input('enter the 2nd sub marks:'))
m3=float(input('enter the 3rd sub marks:'))

totalmarks= m1+m2+m3
print('total marks:',totalmarks)

p=totalmarks/300 *100
print('percentage:',round(p,2))

if p>=60:
    print('1st division')
elif p>=45:                #p<60
    print('2nd division')
elif p>=33:                #p<45:
    print('3rd division')
else:
    print('fail')


