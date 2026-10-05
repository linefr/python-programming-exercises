# Delete potato from prices_copy.db
import sqlite3
from contextlib import closing

with sqlite3.connect("prices_copy.db") as connection:
    with closing(connection.cursor()) as cursor:
        cursor.execute(""" delete from prices
                            where product = "potato" """)
        print('Deleted records: ', cursor.rowcount )
        if cursor.rowcount == 1:
            connection.commit()
            print('changes saved')
        else:
            connection.rollback()
            print('unsaved changes')