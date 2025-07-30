sp=2
st=1
for i in range(1,6):
    for j in range(sp):
        print(' ',end='')
    for k in range(st):
        print('*',end='')
    print()
    if i<=2:
        sp-=1
        st+=2
    else:
        sp+=1
        st-=2
