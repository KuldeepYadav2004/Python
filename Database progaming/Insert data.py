from sqlite3 import *

name=input("Enter Name:")
age=int(input("Enter age:"))
city=input("Enter city:")

con=connect("/Users/kuldeepyadav/Developer/Code/Python/Database progaming/Person.db") #Connecting to the database
cur=con.cursor() #Creating a cursor object
cur.execute("insert into Person(Name,age,city) values(?,?,?)",(name,age,city)) #putting the sql query into the cursor object 
con.commit()# fireing the sql query
con.close()#closing the database connection
print("Data is saved successfully")

