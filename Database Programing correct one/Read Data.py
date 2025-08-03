from sqlite3 import *

con = connect('persons.db') #Connecting to database

cur = con.cursor() #Creating cursor object
cur.execute("select * from person") #Putting the sql query into cursor object and executing the query
persons = cur.fetchall()

con.close() #Closing the database connection

#print(persons)

for person in persons:
    #print(person)
    print("\nId:", person[0])
    print("Name:", person[1])
    print("Age:", person[2])
    print("City:", person[3])
