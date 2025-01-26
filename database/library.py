import sqlite3

# Connect to the database 'library.sqlite3'
conn = sqlite3.connect('database/library.sqlite3')
cursor = conn.cursor()

# Function to create the 'library' table
# def create_table():
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS library (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name_of_student TEXT,
#             faculty TEXT,
#             sem TEXT,
#             books TEXT
#         )
#     ''')
#     conn.commit()
#     print("Table created successfully")

# Function to insert data into the 'library' table
# def insert_data(id, name_of_student, faculty, sem, books):
#     cursor.execute('''
#         INSERT INTO library (id, name_of_student, faculty, sem, books)
#         VALUES (?, ?, ?, ?, ?)
#     ''', (id, name_of_student, faculty, sem, books))
#     conn.commit()
#     print("Data inserted successfully")

# # Call the create_table function to ensure the table exists
# create_table()

# # Input data from the user
# id = int(input("Enter ID: "))
# name_of_student = input("Enter name of the student: ")
# faculty = input("Enter faculty: ")
# sem = input("Enter semester: ")
# books = input("Enter book name(s): ")

# # Insert the user-provided data into the table
# insert_data(id, name_of_student, faculty, sem, books)

# ///////display record
# def show_record():
#     # cursor.execute(""" SELECT *  FROM library""")
#     cursor.execute(""" SELECT *  FROM library where faculty="bca" """)
#     data = cursor.fetchall()
#     # data= cursor.fetchone()
#     # data = cursor.fetchmany(2)
#     print(data)
# show_record()


# def delete():
#     cursor.execute(""" DELETE FROM library WHERE id=1 """)
#     conn.commit()
#     print('delete successfully')
# delete()

def update(name_of_student, faculty, sem, books,id):
    cursor.execute("""UPDATE library SET name_of_student=?, faculty=?, sem=?, books=? WHERE id=? """,(name_of_student, faculty, sem, books, id))
    conn.commit()
    print("update successfully")
update('bibash','bca','vii','ramyan',10 )