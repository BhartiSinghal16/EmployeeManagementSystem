import sqlite3

conn = sqlite3.connect('employees.db')
conn.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    post TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL
)
''')
conn.close()
print("Database created successfully!")
