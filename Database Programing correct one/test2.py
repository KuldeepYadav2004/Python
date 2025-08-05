import os
import sqlite3

# Ensure folder exists before connecting
os.makedirs('Database Programing correct one', exist_ok=True)
conn = sqlite3.connect('/Users/kuldeepyadav/Developer/Code/Python/Database Programing correct one/Queries.sql')
