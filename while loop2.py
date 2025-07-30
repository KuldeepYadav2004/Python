s=0
while True:
    v=input('Enter a number(Enter s to stop ): ')
    if v=='s' or v=='S':
        break

    s+=int(v)
        
print('sum:',s)
