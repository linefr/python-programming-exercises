# Add state_abbreviation and region_abbreviation fields
import sqlite3

data = [
    ["CA", "W", "California"],
    ["TX", "S", "Texas"],
    ["FL", "S", "Florida"],
    ["NY", "NE", "New York"],
    ["PA", "NE", "Pennsylvania"],
    ["IL", "MW", "Illinois"],
    ["OH", "MW", "Ohio"],
    ["GA", "S", "Georgia"],
    ["NC", "S", "North Carolina"],
    ["MI", "MW", "Michigan"],
    ["NJ", "NE", "New Jersey"],
    ["VA", "S", "Virginia"],
    ["WA", "W", "Washington"],
    ["AZ", "W", "Arizona"],
    ["MA", "NE", "Massachusetts"],
    ["TN", "S", "Tennessee"],
    ["IN", "MW", "Indiana"],
    ["MD", "S", "Maryland"],
    ["MO", "MW", "Missouri"],
    ["WI", "MW", "Wisconsin"]
]

with sqlite3.connect('us.db') as connection:
    connection.executemany(""" update states
                            set state_abbreviation = ?,
                            region_abbreviation = ?
                            where name = ?
                            """ ,data)
    connection.commit()