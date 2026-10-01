import sqlite3

con = sqlite3.connect("prices.db")
cur = con.cursor()

product_ask = input("What's the product do you want?")
cur.execute("select * from prices where product = ?", (product_ask,))
while True:
    result = cur.fetchone()
    if result is None:
        print("Sorry, this product doesn't have in database")
        break
    name_product , prices = result

    print(f"name product: {name_product} --> ${prices}")
    break
   


cur.close()
con.close()
