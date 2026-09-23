# Create my first SQLite database with Python

import sqlite3

# One execute() with an INSERT inserts one record (one row).
data = [
    ("potato", 1.20),
    ("banana", 0.99),
    ("strawberry", 2.99),
]

con = sqlite3.connect("prices.db")
cursor = con.cursor()

cursor.execute("""
    CREATE TABLE prices (
        product TEXT,
        price REAL
    )
""")

cursor.executemany("""
    INSERT INTO prices (product, price)
    VALUES (?, ?)
""", data)

con.commit()

cursor.close()
con.close()