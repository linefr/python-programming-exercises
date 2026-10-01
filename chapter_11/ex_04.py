import sqlite3

con = sqlite3.connect("prices.db")
cur = con.cursor()

first_value = float(input("First price: "))
second_value = float(input("Second price: "))
cur.execute("select * from prices where price between ? and ? order by price ", (first_value,second_value))
while True:
    result = cur.fetchone()
    if result is None:
        break
    name_product , prices = result

    print(f"name product: {name_product} --> ${prices}")
   


cur.close()
con.close()
