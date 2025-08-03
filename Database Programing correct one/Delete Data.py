from sqlite3 import *

person_id = int(input("Enter person id: "))

con = connect('persons.db') #Connecting to database

cur = con.cursor() #Creating cursor object
cur.execute("delete from person where Id = ?", (person_id,)) #Putting the sql query into cursor object 
con.commit() #Executing the SQL query

con.close() #Closing the database connection

print("Data is deleted successfully")
