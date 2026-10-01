import sqlite3
from contextlib import closing

with sqlite3.connect("prices.db") as conection:
    with closing(conection.cursor()) as cursor:
        cursor.execute("""update prices
                            set price = 3.99
                            where product = "potato"
                        """)
    conection.commit()