# 1. Introduction to Modules in Python
# A module is a file that contains Python definitions and statements. It allows you to organize and reuse code efficiently.

# ////Creating a Module:

# To create a module, simply save your Python code in a file with a .py extension.
# For example, a file math_operations.py can contain functions like:
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b
# Using a Module:

# You can import the module into other Python files using import:
# import math_operations

# result = math_operations.add(10, 5)
# print(result)  # Output: 15
# Importing Specific Functions:

# You can import only specific functions from a module using from:
# from math_operations import add

# result = add(10, 5)
# print(result)  # Output: 15
# Alias for Modules:

# You can give an alias to a module to make the code more concise:
# import math_operations as mo

# result = mo.add(10, 5)
# print(result)  # Output: 15
# 2. Advanced Concepts in Modules
# Built-in Modules: Python has many built-in modules like os, sys, math, datetime, etc. You can import them the same way as custom modules.

# For example:
# import math
# print(math.sqrt(16))  # Output: 4.0
# Creating Packages:

# A package is a directory that contains multiple Python modules. You can structure your code into packages by creating a directory with __init__.py (even an empty file).
# Example directory structure:

# markdown
# mypackage/
#     __init__.py
#     module1.py
#     module2.py
# To use the package:

# from mypackage import module1
# Module Search Path:

# Python searches for modules in directories listed in the sys.path. You can modify sys.path to add your custom directories.
# 3. Introduction to File Handling in Python
# File handling in Python allows you to work with files such as reading from or writing to them.

# Opening a File:

# You open a file using the open() function.
# file = open('example.txt', 'r')  # 'r' mode is for reading
# File Modes:

# 'r': Read (default mode)
# 'w': Write (overwrites file)
# 'a': Append (adds to the end of the file)
# 'b': Binary mode (e.g., 'rb' for reading in binary)
# 4. Basic File Operations (Beginner Level)
# Reading from a File:
# file = open('example.txt', 'r')
# content = file.read()  # Reads the entire file
# print(content)
# file.close()
# Writing to a File:
# file = open('example.txt', 'w')
# file.write("Hello, world!")
# file.close()
# Appending to a File:
# file = open('example.txt', 'a')
# file.write("\nAppended text.")
# file.close()
# 5. Working with File Handling in Python (Intermediate Level)
# Reading File Line by Line:

# file = open('example.txt', 'r')
# for line in file:
#     print(line.strip())  # strip() removes trailing newline characters
# file.close()
# Reading a File into a List:
# file = open('example.txt', 'r')
# lines = file.readlines()  # Returns a list of lines
# file.close()
# for line in lines:
#     print(line.strip())
# Context Manager (with statement):

# Using the with statement is recommended as it ensures the file is properly closed, even if an error occurs.
# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)
# 6. Advanced File Handling Techniques
# Handling Binary Files:

# When working with binary files (like images), use 'rb' or 'wb' mode.
# with open('example.jpg', 'rb') as file:
#     data = file.read()
# File Seeking:

# You can move the file pointer to a specific position using seek():
# with open('example.txt', 'r') as file:
#     file.seek(10)  # Moves pointer to the 10th byte
#     print(file.read())
# File Truncating:

# You can remove the content of a file by truncating it:
# with open('example.txt', 'w') as file:
#     file.truncate(0)  # Empties the file
# Working with CSV Files:

# Python has a csv module to handle CSV files easily.
# import csv
# with open('data.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
# Writing to CSV:
# import csv
# data = [['Name', 'Age'], ['Alice', 25], ['Bob', 30]]
# with open('output.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)
# 7. Error Handling with File Operations
# Handling Errors:

# Use try...except blocks to catch and handle file-related errors.
# try:
#     with open('nonexistentfile.txt', 'r') as file:
#         content = file.read()
# except FileNotFoundError:
#     print("The file was not found.")
# except Exception as e:
#     print(f"An error occurred: {e}")
# Handling File Not Found Error:
# try:
#     file = open('file.txt', 'r')
# except FileNotFoundError:
#     print("File does not exist.")
# 8. Conclusion: Mastering Modules and File Handling
# Modules and file handling are core concepts in Python, used for organizing code and working with external data.
# Modules help you organize and reuse code, while file handling allows you to interact with external data stored in files.
# As you advance, you’ll work with complex file formats (JSON, CSV, XML) and utilize modules like os for managing files and directories.