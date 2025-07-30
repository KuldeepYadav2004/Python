import random
values=[12,2,3,23,34]
for i in range(5):
    print(random.choice(values))


for i in range(5):
    random.shuffle(values)
    print(values)
for i in range(5):
    print(random.randint(0,9))
    
