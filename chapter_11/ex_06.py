import sqlite3
from contextlib import closing

with sqlite3.connect('prices.db') as connection:
    
    with closing(connection.cursor()) as cursor:
        product_ask = input('Name product: ')
        new_price = input('New price: ')
        cursor.execute(""" update prices
                                set price = ? 
                                where product = ?""", (new_price, product_ask))
    connection.commit()
