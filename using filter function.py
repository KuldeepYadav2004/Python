def iseven(n):
    return n%2==0
numbers =[12,2,3,23,34]
even_numbers = list(filter(iseven,numbers))
print(even_numbers)
