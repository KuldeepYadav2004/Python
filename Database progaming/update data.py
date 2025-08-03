from sqlite3 import *
person_id=int(input("Enter Person Id:"))
name=input("Enter New Name:")
age=int(input("Enter New age:"))
city=input("Enter New city:")

con=connect('Person.db') #Connecting to the database
cur=con.cursor() #Creating a cursor object
cur.execute("update  Person set name=?,age=?,city=? where Id=?"(name,age,city,person_id)) #putting the sql query into the cursor object 
con.commit()# fireing the sql query
con.close()#closing the database connection
print("Data is saved successfully")

