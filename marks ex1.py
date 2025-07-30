m1=int(input('enter the 1st sub marks:'))
m2=int(input('enter the 2nd sub marks:'))
m3=int(input('enter the 3rd sub marks:'))

totalmarks= m1+m2+m3
print('total marks:',totalmarks)
if totalmarks>=150:
    print('result=pass')
else:
    print('result=fail')
