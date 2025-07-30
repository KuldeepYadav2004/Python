values =set()
print(type(values))
while True:
    values.add(int(input("Enter a number:")))
    print(values)
    ch=input("Enter yes to continue:")
    if ch.lower() !='yes':
        break