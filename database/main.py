import sqlite3
conn = sqlite3.connect('database/college.sqlite3')#database name college extension sqlite3

cursor = conn.cursor()#cursor object instences code haru line khojeko

# def create_table():
#      # double or single cootetion  rakhe multiline lekhne milxa, executele lekheko code mileko x ki nai verify
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS student (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             email TEXT,
#             age INTEGER,
#             address TEXT
#         )
#     ''')
#     conn.commit()#commit le structure  thik vya apply
#     print('table created sucessfully')

# create_table()#call method/function create_table, table create vay paxi yo call garnu parena


# def insert_data(name,email,age,address):
#     cursor.execute("""INSERT INTO student(name,email,age,address) VALUES(?,?,?,?)""",(name,email,age,address))
#     conn.commit()
#     print("Data inserted sucesfully..")


# name = input('enter your name:')
# email = input('enter your email:')
# age = int(input('enter your ager:'))
# address = input('enter your address:')
# #pass data to insert
# insert_data(name,email,age,address)


# ////////////////display record......
# def show_record():
#     cursor.execute(""" SELECT *  FROM student""")
#     # cursor.execute(""" SELECT *  FROM student where id=1""")
#     data = cursor.fetchall()
#     # data= cursor.fetchone()
#     # data = cursor.fetchmany(2)
#     print(data)
# show_record()


# def delete():
#     cursor.execute(""" DELETE FROM student WHERE id=5 """)
#     conn.commit()
#     print("deleted successfully")
# delete()


# def update(name,email,age,address,id):
#     cursor.execute(""" UPDATE student SET name=?,email=?,age=?,address=? WHERE ID=?""",(name,email,age,address,id))
#     conn.commit()
#     print("updated successfully")
# update('razz','raz@gmail.com',34,'olulu',8)

