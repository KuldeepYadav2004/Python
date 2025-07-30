for i in range(1,101):
    if i==1:
        continue
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,'is a prime number')
