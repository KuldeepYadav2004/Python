def add(*numbers):
    s=0
    for n in numbers:
        s+=n
    return s
print(add(12,2,23))
print(add(12,23))
print(add(12,2,3))

