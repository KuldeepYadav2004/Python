from sqlite3 import *

person_id = int(input("Enter person id: "))
name = input("Enter new name: ")
age = int(input("Enter new age: "))
city = input("Enter new city: ")

con = connect('persons.db') #Connecting to database

cur = con.cursor() #Creating cursor object
cur.execute("update person set name = ?, age = ?, city = ? where Id = ?", (name, age, city, person_id)) #Putting the sql query into cursor object 
con.commit() #Executing the SQL query

con.close() #Closing the database connection

print("Data is updated successfully")
