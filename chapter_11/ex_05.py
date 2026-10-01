import sqlite3
from contextlib import closing

pct = 0.1
with sqlite3.connect("prices.db") as connection:
    with closing(connection.cursor()) as cursor:
        cursor.execute(""" update prices
                            set price = 1.1 * price 
                        """)
    connection.commit()