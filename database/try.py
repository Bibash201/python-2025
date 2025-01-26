import sqlite3

# Connect to the database 'product.sqlite3'
conn = sqlite3.connect('database/product.sqlite3')
cursor = conn.cursor()

# Function to create the 'product' table
# def create_table():
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS product (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             quantity INTEGER,
#             price INTEGER,
#             total INTEGER
#         )
#     ''')
#     conn.commit()
#     print("Product table created successfully")

# # # Function to insert data into the 'product' table
# def insert_data(name, quantity, price, total):
#     cursor.execute('''INSERT INTO product (name, quantity, price, total) VALUES (?, ?, ?, ?)''', (name, quantity, price, total))
#     conn.commit()
#     print("Data inserted successfully")

# # Call the create_table function to ensure the table exists
# create_table()

# # Input data from the user
# name = input("Enter the name of the product: ")
# quantity = int(input("Enter the quantity of the product: "))
# price = int(input("Enter the price of the product: "))
# total = price * quantity

# # Insert the user-provided data into the table
# insert_data(name, quantity, price, total)

# ///////display record
# def show_record():
#     cursor.execute(""" SELECT *  FROM product""")
#     # cursor.execute(""" SELECT *  FROM product where id=1""")
#     data = cursor.fetchall()
#     # data= cursor.fetchone()
#     # data = cursor.fetchmany(2)
#     print(data)
# show_record()


# def delete():
#     cursor.execute(""" DELETE FROM product where name='ramba' """)
#     conn.commit()
#     print("delete successfully")
# delete()


def update(name, quantity, price, total, id):
    cursor.execute(""" UPDATE product SET name=?,quantity=?,price=?,total=? WHERE id=?""",(name,quantity,price,total,id))
    conn.commit()
    print("updated successfully")
update('wai_wai',100,20,2000,2)