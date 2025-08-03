from sqlite3 import *
person_id=int(input("Enter Person Id:"))


con=connect('Person.db') #Connecting to the database
cur=con.cursor() #Creating a cursor object
cur.execute("delete from  Person where  Id=?"(person_id)) #putting the sql query into the cursor object 
con.commit()# fireing the sql query
con.close()#closing the database connection
print("Data is saved successfully")

