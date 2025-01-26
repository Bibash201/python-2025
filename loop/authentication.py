
# category =[
#     {'cid':1,'name':'Electronics'},
#     {'cid':2,'name':'Clothing'},
#     {'cid':3,'name':'Grocery'},
# ]


# products=[
#     {'pid':1,'name':'Mobile','price':20000,'quantity':2,'cid':1},
#     {'pid':2,'name':'Laptop','price':50000,'quantity':1,'cid':1},
#     {'pid':3,'name':'T-shirt','price':500,'quantity':3,'cid':2},
#     {'pid':4,'name':'Jeans','price':1500,'quantity':2,'cid':2},
#     {'pid':5,'name':'Rice','price':50,'quantity':5,'cid':3},
#     {'pid':6,'name':'Dal','price':100,'quantity':2,'cid':3},
# ]

# name = input(f"Enter the category name: ")
# for cat in category:
#     if cat['name']==name:
#         for product in products:
#             if product['cid']==cat['cid']:
#                 total = product['price'] * product['quantity']
#                 print(f"Product Name: {product['name']} Price: {product['price']}  Quantity: {product['quantity']}  Total: {total}")


# users=[
#     {'username':'admin','password':'admin'},
#     {'username':'ram','password':'ram'},
# ]

# products=[
#     {'pid':1,'name':'Mobile','price':20000,'quantity':2,'cid':1},
#     {'pid':2,'name':'Laptop','price':50000,'quantity':1,'cid':1},
#     {'pid':3,'name':'T-shirt','price':500,'quantity':3,'cid':2},
#     {'pid':4,'name':'Jeans','price':1500,'quantity':2,'cid':2},
#     {'pid':5,'name':'Rice','price':50,'quantity':5,'cid':3},
#     {'pid':6,'name':'Dal','price':100,'quantity':2,'cid':3},
# ]






# List of users with their username and password
# users = [
#     {'username': 'admin', 'password': 'admin'},
#     {'username': 'ram', 'password': 'ram'},
# ]

# # Prompt the user to input their username
# username = input("Enter your username: ").strip()  # Remove any leading/trailing spaces from the input

# # Prompt the user to input their password
# password = input("Enter your password: ").strip()  # Remove any leading/trailing spaces from the input

# # Initialize a variable to store the logged-in user if credentials match
# logged_in_user = None

# # Iterate through the list of users to find a match
# for user in users:
#     # Check if the entered username and password match the current user's credentials
#     if user['username'] == username and user['password'] == password:
#         logged_in_user = user  # Store the matched user
#         break  # Exit the loop as we found a match

# # Check if a valid user was found
# if logged_in_user:
#     # If a match was found, print a welcome message with the username
#     print(f"Welcome, {logged_in_user['username']}!")
# else:
#     # If no match was found, inform the user of invalid credentials
#     print("Invalid username or password. Please try again.")





# # List of faculties, each having a unique faculty ID (fid) and name
# faculty = [
#     {'fid': 1, 'name': 'Science'},
#     {'fid': 2, 'name': 'Management'},
#     {'fid': 3, 'name': 'Humanities'},
# ]

# # List of students, each having a unique student ID (sid), name, and associated faculty ID (fid)
# students = [
#     {'sid': 1, 'name': 'ram', 'fid': 1},
#     {'sid': 2, 'name': 'sita', 'fid': 2},
#     {'sid': 3, 'name': 'gita', 'fid': 3},
#     {'sid': 4, 'name': 'gopal', 'fid': 1},
#     {'sid': 5, 'name': 'hari', 'fid': 2},
#     {'sid': 6, 'name': 'nabin', 'fid': 3},
#     {'sid': 7, 'name': 'sabin', 'fid': 1},
#     {'sid': 8, 'name': 'abinash', 'fid': 2},
#     {'sid': 9, 'name': 'anil', 'fid': 3},
#     {'sid': 10, 'name': 'santosh', 'fid': 1},
# ]

# # Prompt the user to input the name of a faculty
# faculty_name = input("Enter the faculty name: ").strip()  # Remove any leading or trailing spaces

# # Loop through each faculty to find the one matching the user input
# for fac in faculty:
#     if fac['name'].lower() == faculty_name.lower():  # Case-insensitive match for the faculty name
#         print(f"\nStudents in the {fac['name']} faculty:\n")
#         # Loop through the students to find those belonging to the matched faculty
#         for student in students:
#             if student['fid'] == fac['fid']:  # Match the faculty ID (fid)
#                 # Display the student's details
#                 print(f"Student ID: {student['sid']} Name: {student['name']}")
              
#         break
# else:
#     # If no matching faculty is found, display an appropriate message
#     print("No such faculty found. Please check the name and try again.")



# # List of faculties, each having a unique faculty ID (fid) and name
# faculty = [
#     {'fid': 1, 'name': 'Science'},
#     {'fid': 2, 'name': 'Management'},
#     {'fid': 3, 'name': 'Humanities'},
# ]

# # List of students, each having a unique student ID (sid), name, and associated faculty ID (fid)
# students = [
#     {'sid': 1, 'name': 'ram', 'fid': 1},
#     {'sid': 2, 'name': 'sita', 'fid': 2},
#     {'sid': 3, 'name': 'gita', 'fid': 3},
#     {'sid': 4, 'name': 'gopal', 'fid': 1},
#     {'sid': 5, 'name': 'hari', 'fid': 2},
#     {'sid': 6, 'name': 'nabin', 'fid': 3},
#     {'sid': 7, 'name': 'sabin', 'fid': 1},
#     {'sid': 8, 'name': 'abinash', 'fid': 2},
#     {'sid': 9, 'name': 'anil', 'fid': 3},
#     {'sid': 10, 'name': 'santosh', 'fid': 1},
# ]

# # Prompt the user to input the name of a faculty
# faculty_name = input("Enter the faculty name: ").strip()  # Remove any leading or trailing spaces

# # Loop through each faculty to find the one matching the user input
# for fac in faculty:
#     if fac['name'].lower() == faculty_name.lower():  # Case-insensitive match for the faculty name
#         print(f"\nStudents in the {fac['name']} faculty:\n")
        
#         # Find students in the selected faculty
#         students_in_faculty = [student for student in students if student['fid'] == fac['fid']]
        
#         # Display student details
#         for student in students_in_faculty:
#             print(f"Student ID: {student['sid']} Name: {student['name']}")
        
#         # Print the total number of students under the faculty
#         print(f"\nTotal students in {fac['name']} faculty: {len(students_in_faculty)}")
#         break
# else:
#     # If no matching faculty is found, display an appropriate message
#     print("No such faculty found. Please check the name and try again.")



# faculty = [
#     {'fid': 1, 'name': 'Science'},
#     {'fid': 2, 'name': 'Management'},
#     {'fid': 3, 'name': 'Humanities'},
# ]

# students = [
#     {'sid': 1, 'name': 'ram', 'fid': 1},
#     {'sid': 2, 'name': 'sita', 'fid': 2},
#     {'sid': 3, 'name': 'gita', 'fid': 3},
#     {'sid': 4, 'name': 'gopal', 'fid': 1},
#     {'sid': 5, 'name': 'hari', 'fid': 2},
#     {'sid': 6, 'name': 'nabin', 'fid': 3},
#     {'sid': 7, 'name': 'sabin', 'fid': 1},
#     {'sid': 8, 'name': 'abinash', 'fid': 2},
#     {'sid': 9, 'name': 'anil', 'fid': 3},
#     {'sid': 10, 'name': 'santosh', 'fid': 1},
# ]
# faculty = [
#     {'fid': 1, 'name': 'Science'},
#     {'fid': 2, 'name': 'Management'},
#     {'fid': 3, 'name': 'Humanities'},
# ]

# students = [
#     {'sid': 1, 'name': 'ram', 'fid': 1},
#     {'sid': 2, 'name': 'sita', 'fid': 2},
#     {'sid': 3, 'name': 'gita', 'fid': 3},
#     {'sid': 4, 'name': 'gopal', 'fid': 1},
#     {'sid': 5, 'name': 'hari', 'fid': 2},
#     {'sid': 6, 'name': 'nabin', 'fid': 3},
#     {'sid': 7, 'name': 'sabin', 'fid': 1},
#     {'sid': 8, 'name': 'abinash', 'fid': 2},
#     {'sid': 9, 'name': 'anil', 'fid': 3},
#     {'sid': 10, 'name': 'santosh', 'fid': 1},
# ]

# faculty_name = input("Enter faculty name: ")

# # Check for the input faculty name
# for fac in faculty:
  
#         print(f"\nStudents in {fac['name']} faculty:")
#         student_list = []

#         for st in students:
#             if st['fid'] == fac['fid']:
#                 student_list.append(st)
#                 print(f"Student ID: {st['sid']}, Name: {st['name']}, Faculty ID: {st['fid']}")

#         # Print total count after listing all students
#         print(f"\nTotal students in {fac['name']} faculty: {len(student_list)}")
#         break




# # Prompt the user to input the name of a faculty
# faculty_name = input("Enter the faculty name: ").strip()


# for fac in faculty:
  
#         print(f"\nStudents in the {fac['name']} faculty:\n")
        
#         # Find students in the selected faculty using a basic loop
#         students_in_faculty = []
#         for student in students:
#             if student['fid'] == fac['fid']:
#                 students_in_faculty.append(student)
#                 print(f"Sid: {student['sid']} Name: {student['name']} fid:{student['fid']}")
        
#         # Print the total number of students under the faculty
#         print(f"\nTotal students in {fac['name']} faculty: {len(students_in_faculty)}")
#         break










users = [
    {'username': 'admin', 'password': 'admin'},
    {'username': 'ram', 'password': 'ram'},
]

username = input("Enter your username: ")
password = input("Enter your password: ")

# for user in users: 
#     if user['username'] == username and user['password'] == password:       
#         print(f"Welcome, {username}!")
#         break 
# else:
#       print("Invalid username or password. Please try again.")

for user in users:
    if user['username']==username:
        if user['password']==password:
            print(f"welcome{username}")
        else:
            print("wrong pass")
            break
    
    else:
        print("wrong username")
        break


# users = [
#      {'username': 'admin', 'password': 'admin'},
#      {'username': 'ram', 'password': 'ram'},
# ]
# uname=input("enter uname:")
# pw=input("enter pw:")
# for user in users:
#     if user['username']==uname:
#         if user['password']==pw:
#             print(f"welcome {uname}")
            
#         else:
#             print("wrong pw")
#             
            

#     else:
#         print("wrong uname")


users = [
    {'username': 'admin', 'password': 'admin'},
    {'username': 'ram', 'password': 'ram'},
]

# Prompt the user to enter username and password
uname = input("Enter username: ")
pw = input("Enter password: ")

# Flag to check if the username exists
user_found = False

# Iterate over the users to validate credentials
for user in users:
    if user['username'] == uname:
        user_found = True  # Username exists
        if user['password'] == pw:
            print(f"Welcome {uname}!")
        else:
            print("Wrong password.")
        break

# If username is not found in the loop
if not user_found:
    print("Wrong username.")
