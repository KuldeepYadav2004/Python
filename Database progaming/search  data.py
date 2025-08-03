from sqlite3 import *
person_id=int(input("Enter person id :"))


con=connect('Person.db') #Connecting to the database
cur=con.cursor() #Creating a cursor object
cur.execute("select * from Person where Id=?",(person_id)) #putting the sql query into the cursor object 
persons=cur.fetchone()
con.close()#closing the database connection
#print(persons)
if person is not None:
    print("\nId:",person[0])
    print("Name::",person[1])
    print("age:",person[2])
    print("city:",person[3])
else:
    print("Person does not exists with this id:")



