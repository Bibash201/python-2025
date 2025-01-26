import sqlite3

# Connect to the database 'user.sqlite3'
conn = sqlite3.connect('database/user.sqlite3')
cursor = conn.cursor()

# Function to create the 'user' table
# def create_table():
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS user (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             userid INTEGER,
#             name TEXT,
#             email TEXT,
#             department TEXT,
#             slry INTEGER
#         )
#     ''')
#     conn.commit()
#     print("User table created successfully")

# # Function to insert data into the 'user' table
# def data_insert(userid, name, email, department, slry):
#     cursor.execute('''
#         INSERT INTO user (userid, name, email, department, slry)
#         VALUES (?, ?, ?, ?, ?)
#     ''', (userid, name, email, department, slry))
#     conn.commit()
    
#     notic="inserted successfuly"
#     print(f"{notic}")

# # Call the create_table function to ensure the table exists
# create_table()

# # Input data from the user
# userid = int(input("Enter user ID: "))
# name = input("Enter user name: ")
# email = input("Enter user email: ")
# department = input("Enter user department: ")
# slry = int(input("Enter user salary: "))

# # Insert the user-provided data into the table
# data_insert(userid, name, email, department, slry)


# def show_record():
#     cursor.execute(""" SELECT *  FROM user""")
#     # cursor.execute(""" SELECT *  FROM user where id=1""")
#     data = cursor.fetchall()
#     # data= cursor.fetchone()
#     # data = cursor.fetchmany(2)
#     print(data)
# show_record()


# ////delete record
# def delete_record():
#     try:
#         # Assuming the database connection is already established and `cursor` is defined
#         cursor.execute("""DELETE FROM USER WHERE id=  """)
#         # Commit the changes to the database
#         conn.commit()
#         print("Deleted successfully")
#     except Exception as e:
#         print("An error occurred:", e)

# # Call the function
# delete_record()


def update(name, email, department, slry, userid):
    cursor.execute('''UPDATE user SET name=?, email=?, department=?, slry=? WHERE userid=? ''', (name, email, department, slry, userid))
    conn.commit()
    print("update success")
update('jhon','jhon@gmail.com','cleaning',20000,78)

