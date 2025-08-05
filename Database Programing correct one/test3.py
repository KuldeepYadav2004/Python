import sqlite3

conn = sqlite3.connect('Person.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Person (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
''')
conn.commit()
