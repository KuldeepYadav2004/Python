n=int(input('enter number of sub:'))
t=0
for i in range(1,n+1):
     m=int(input('enter marks of subject '+str(i)+":"))
     t=t+m
print('Total of marks:',t)
a=t/n
print('avg. marks :',round(a,2))

