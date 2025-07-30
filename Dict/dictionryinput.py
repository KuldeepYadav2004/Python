contacts ={}
print(type(contacts))
print(contacts)

while True:
    phone_number = input("Enter phone number:")
    if phone_number not in contacts:
        contacts[phone_number]=input("Enter name:")
    else:
        print(phone_number,"is already added")
    ch= input("Do you want to continue?[yes/no]:")
    if ch.lower() != 'yes':
        break
print("All contact details are")
for phone_number in contacts:
    print(phone_number,'-->',contacts[phone_number])
    
