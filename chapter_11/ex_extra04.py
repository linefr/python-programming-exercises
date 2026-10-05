# Order by population 
import sqlite3

with sqlite3.connect("us.db") as connection:
    connection.row_factory = sqlite3.Row
    for state in connection.execute("select * from states order by population desc"):
        print(f"{state['id']:3d}: {state['name']:>20s}  {state['population']:12d}")

        