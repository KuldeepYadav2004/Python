def factorial(n):
    if n>1:
        return n * factorial(n-1)
    else:
        return 1

n=int(input('Enter a number:'))
f=factorial(n)
print('Factorial:',f)
