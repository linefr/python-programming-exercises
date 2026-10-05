# Delete potato from prices_copy.db
import sqlite3
from contextlib import closing

data = [
    ["California", 39538223],
    ["Texas", 29145505],
    ["Florida", 21538187],
    ["New York", 20201249],
    ["Pennsylvania", 13002700],
    ["Illinois", 12812508],
    ["Ohio", 11799448],
    ["Georgia", 10711908],
    ["North Carolina", 10439388],
    ["Michigan", 10077331],
    ["New Jersey", 9288994],
    ["Virginia", 8631393],
    ["Washington", 7705281],
    ["Arizona", 7151502],
    ["Massachusetts", 7029917],
    ["Tennessee", 6910840],
    ["Indiana", 6785528],
    ["Maryland", 6177224],
    ["Missouri", 6154913],
    ["Wisconsin", 5893718]
]


with sqlite3.connect("us.db") as connection:
    with closing(connection.cursor()) as cursor:
        cursor.execute(""" create table states(
                                id integer primary key autoincrement,
                                name text,
                                population integer)""")
        cursor.executemany("""insert into states (name, population) values(?,?)""",data)
        connection.commit()
       