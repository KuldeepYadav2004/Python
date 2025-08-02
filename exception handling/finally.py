try:
    n1=int(input('Enter first number:'))
    n2=int(input("Enter second number:"))
    r=n1/n2
except Exception:
    print('something went wrong')
else:
    print("Result:",r)
finally:
    print("This will be always executed  ")
print('Hello')
