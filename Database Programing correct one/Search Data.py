from sqlite3 import *

person_id = int(input("Enter person id: "))

con = connect('persons.db') #Connecting to database

cur = con.cursor() #Creating cursor object
cur.execute("select * from person where Id = ?", (person_id,)) #Putting the sql query into cursor object and executing the query
person = cur.fetchone()

con.close() #Closing the database connection

#print(person)

if person is not None:
    print("Person Id:", person[0])
    print("Name:", person[1])
    print("Age:", person[2])
    print("City:", person[3])
else:
    print("Person does not exist")

