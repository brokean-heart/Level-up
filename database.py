import sqlite3

conn = sqlite3.connect("darkside.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts(

id INTEGER PRIMARY KEY AUTOINCREMENT,

name TEXT NOT NULL,

email TEXT NOT NULL,

message TEXT NOT NULL

)
""")

conn.commit()

conn.close()

print("Database Created Successfully")