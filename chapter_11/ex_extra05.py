# altering the table
import sqlite3

with sqlite3.connect('us.db') as connection:
    connection.execute("""alter table states
                            add state_abbreviation text """)
    connection.execute("""alter table states
                            add region_abbreviation text """)