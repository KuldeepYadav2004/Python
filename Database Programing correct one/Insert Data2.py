from sqlite3 import *

name = input("Enter name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")

con = connect("/Users/kuldeepyadav/Developer/Code/Python/Database Programing correct one/persons.db") #Connecting to database

cur = con.cursor() #Creating cursor object
cur.execute("insert into Person(name, age, city) values(?, ?, ?)", (name, age, city)) #Putting the sql query into cursor object 
con.commit() #Firing the SQL query

con.close() #Closing the database connection

print("Data is saved successfully")
