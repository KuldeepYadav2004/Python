def add(n1,n2,n3= None):
    if n3 is None:
        return n1+n2
    else:
        return n1+n2+n3

print(add(12,23))
print(add(12,2,23))
