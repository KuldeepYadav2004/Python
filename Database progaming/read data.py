from sqlite3 import *


con=connect('Person.db') #Connecting to the database
cur=con.cursor() #Creating a cursor object
cur.execute("select * from Person") #putting the sql query into the cursor object 
persons=cur.fetchall()
con.close()#closing the database connection
#print(persons)
for person in persons:
    #print(person)
    print("\nId:",person[0])
    print("Name::",person[1])
    print("age:",person[2])
    print("city:",person[3])



