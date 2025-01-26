import sqlite3

conn = sqlite3.connect('database/productsec.sqlite3')
cursor = conn.cursor()

def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productsec (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price INTEGER NOT NULL
        )
    ''')
    conn.commit()
    # print("Productsec table created successfully")
create_table()

def insert_data(name, quantity, price):
    cursor.execute('''INSERT INTO productsec (name, quantity, price) VALUES (?, ?, ?)''', (name, quantity, price))
    conn.commit()
    print("Data inserted successfully")

# def show_records():
#     cursor.execute("SELECT id, name, quantity, price, (quantity * price) AS total FROM productsec")
#     records = cursor.fetchall()
#     print("ID |    Name    | Quantity | Price | Total ")
#     print("--------------------------------------------")
#     # for record in records:
#     #     print(f"{record[0]} | {record[1]} | {record[2]}      |  {record[3]}   | {record[4]} ")

#     #  :<10->Left-aligns the name within a field of 10 characters wide,:<3(left aligns withnin a field of 3 cheracter)
#     for record in records:
#         print(f"{record[0]:<3}| {record[1]:<10} | {record[2]:<8} | {record[3]:<5} | {record[4]:<5}")
# show_records()

# name = input("Enter the name of the product: ")
# quantity = int(input("Enter the quantity of the product: "))
# price = int(input("Enter the price of the product: "))
# insert_data(name, quantity, price)



# def delete():
#     cursor.execute(''' DELETE FROM productsec WHERE id=2''')
#     conn.commit()
#     print("delete data successfully")
# delete()


# def data_update(name,quantity,price,id):
#     cursor.execute(''' UPDATE productsec SET name=?, quantity=?, price=? WHERE id=?''',(name,quantity,price,id))
#     conn.commit()
#     print("updated successfully..")
# data_update('paralg',300,10,3)





def show():
    cursor.execute("""SELECT id, name, quantity, price, (quantity*price) AS total FROM productsec""")
    record = cursor.fetchall()
    print("ID|  NAME  | QUANTITY | PRICE | TOTAL ")
    print("---------------------------------------")
    for data in record:
        print(f"{data[0]:<2}|{data[1]:<8}|{data[2]:<10}|{data[3]:<7}|{data[4]:<2}")

show()















