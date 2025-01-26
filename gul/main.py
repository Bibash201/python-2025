import tkinter as tk
app = tk.Tk()
app.title("GUI App")
app.geometry("500x400")
fn = tk.Label(app, text="Enter first number")
fn.pack()
n1 = tk.Entry(app)
n1.pack()
sn = tk.Label(app, text="Enter second number")
sn.pack()
n2 = tk.Entry(app)
n2.pack()
result = tk.Label(app, text="Result")
result.pack()
def add():
    first_number = int(n1.get())
    second_number = int(n2.get())
    total = first_number + second_number
    result.config(text="Result: " + str(total))
    n1.delete(0, tk.END)
    n2.delete(0, tk.END)

button = tk.Button(app, text="Add Number", command=add)
button.pack()
app.mainloop()




import tkinter as tk
# Import the tkinter library to create and manage the graphical user interface (GUI).
app = tk.Tk()
# Create the main application window using the Tk class from tkinter.
app.title("GUI App")
# Set the title of the application window to "GUI App."
app.geometry("500x400")
# Define the size of the application window as 500 pixels wide and 400 pixels high.
fn = tk.Label(app, text="Enter first number")
# Create a label widget with the text "Enter first number" and associate it with the main application window (app).
fn.pack()
# Place the fn label in the application window using the pack() method, which automatically arranges it in the layout.
n1 = tk.Entry(app)
# Create an entry widget (Entry) for user input to accept the first number and associate it with the application window.
n1.pack()
# Place the n1 entry widget in the application window using the pack() method.
sn = tk.Label(app, text="Enter second number")
# Create a label widget with the text "Enter second number" and associate it with the main application window (app).
sn.pack()
# Place the sn label in the application window using the pack() method.
n2 = tk.Entry(app)
# Create an entry widget (Entry) for user input to accept the second number and associate it with the application window.
n2.pack()
# Place the n2 entry widget in the application window using the pack() method.
result = tk.Label(app, text="Result")
# Create a label widget with the text "Result" to display the result of the addition and associate it with the main application window.
result.pack()
# Place the result label in the application window using the pack() method.
def add():
# Define a function named add to handle the addition operation when the button is clicked.
    first_number = int(n1.get())
# Retrieve the value from the n1 entry widget, convert it to an integer, and store it in the variable first_number.
    second_number = int(n2.get())
# Retrieve the value from the n2 entry widget, convert it to an integer, and store it in the variable second_number.
    total = first_number + second_number
# Add first_number and second_number to calculate the total.
    result.config(text="Result: " + str(total))
# Update the result label with the calculated total, converting it to a string and appending it to "Result: ".
    n1.delete(0, tk.END)
# Clear the content of the n1 entry widget by deleting all characters from the start (index 0) to the end.
    n2.delete(0, tk.END)
# Clear the content of the n2 entry widget by deleting all characters from the start (index 0) to the end.
button = tk.Button(app, text="Add Number", command=add)
# Create a button widget labeled "Add Number" and set its command to the add function so it executes the function when clicked.
button.pack()
# Place the button in the application window using the pack() method.
app.mainloop()
# Enter the main event loop of the application, keeping the window open and responsive to user interactions.







# import tkinter as tk 
# app = tk.Tk()
# app.title("GUI App")
# app.geometry("500x400")

# fn = tk.Label(app, text="")
# fn.pack()
# n1 = tk.Entry(app)
# n1.pack()

# nine = tk.Button(app, text="9")
# eight  = tk.Button(app, text="8")
# seven = tk.Button(app, text="7")
# six = tk.Button(app, text="6")
# five  = tk.Button(app, text="5")
# four = tk.Button(app, text="4")
# three = tk.Button(app, text="3")
# two = tk.Button(app, text="2")
# one= tk.Button(app, text="1")
# zero = tk.Button(app, text="0")
# cross=tk.Button(app,text="x")
# div=tk.Button(app,text="/")
# mul=tk.Button(app,text="*")
# sub=tk.Button(app,text="-")
# add=tk.Button(app,text="+")
# equal=tk.Button(app,text="=")
# ads=tk.Button(app,text="+/-")
# dot=tk.Button(app,text=".")


# cross.grid(row=0, column=3)

# div.grid(row=1, column=3)



# seven.grid(row=2, column=0)
# eight.grid(row=2, column=1)
# nine.grid(row=2, column=2)
# mul.grid(row=2, column=3)

# four.grid(row=3, column=0)
# five.grid(row=3, column=1)
# six.grid(row=3, column=2)
# sub.grid(row=3, column=3)

# one.grid(row=4, column=0)
# two.grid(row=4, column=1)
# three.grid(row=4, column=2)
# add.grid(row=4, column=3)

# ads.grid(row=5, column=0)
# zero.grid(row=5,column=1)
# equal.grid(row=5, column=3)
# dot.grid(row=5,column=2)


# app.mainloop()



# import tkinter as tk

# def click_button(value):
#     current = entry.get()
#     if value == "=":
#         try:
#             result = eval(current)  # Evaluate the expression
#             entry.delete(0, tk.END)
#             entry.insert(0, str(result))
#         except Exception as e:
#             entry.delete(0, tk.END)
#             entry.insert(0, "Error")
#     elif value == "C":
#         entry.delete(0, tk.END)
#     else:
#         entry.insert(tk.END, value)

# Initialize the main application window
# app = tk.Tk()
# app.title("Calculator")
# app.geometry("400x500")

# Entry widget to display numbers and results
# entry = tk.Entry(app)
# entry.grid(row=0, column=0)

# Define button labels
# buttons = [
#     ("C", 1, 0), ("", 1, 1), ("", 1, 2), ("/", 1, 3),
#     ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
#     ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
#     ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
#     ("+/-", 5, 0), ("0", 5, 1), (".", 5, 2), ("=", 5, 3),
# ]

# Create buttons and place them on the grid
# for text, row, col in buttons:
#     if text:  # Skip empty labels
#         btn = tk.Button(app, text=text)
#         btn.grid(row=row, column=col)

# Adjust row and column weights
# for i in range(6):  # 6 rows
#     app.grid_rowconfigure(i, weight=0)
# for i in range(4):  # 4 columns
#     app.grid_columnconfigure(i, weight=0)

# app.mainloop()





# import tkinter as tk

# def click_button(value):
#     current = entry.get()
#     if value == "=":
#         try:
#             result = eval(current.replace("x", "*"))  # Replace 'x' with '*' for multiplication
#             entry.delete(0, tk.END)
#             entry.insert(0, str(result))
#         except Exception:
#             entry.delete(0, tk.END)
#             entry.insert(0, "Error")
#     elif value == "C":
#         entry.delete(0, tk.END)  # Clear the entire entry
#     elif value == "x":  # Backspace functionality
#         entry.delete(len(current) - 1, tk.END)
#     else:
#         entry.insert(tk.END, value)

# # Initialize the main application window
# app = tk.Tk()
# app.title("GUI App")
# app.geometry("400x500")

# # Set column spacing to 0
# for i in range(4):
#     app.grid_columnconfigure(i, minsize=0)

# # Entry widget to display numbers and results
# entry = tk.Entry(app, justify="center")
# entry.grid(row=0, column=0, columnspan=4, padx=0, pady=10)  # No column padding

# # Buttons
# nine = tk.Button(app, text="9", command=lambda: click_button("9"))
# eight = tk.Button(app, text="8", command=lambda: click_button("8"))
# seven = tk.Button(app, text="7", command=lambda: click_button("7"))
# six = tk.Button(app, text="6", command=lambda: click_button("6"))
# five = tk.Button(app, text="5", command=lambda: click_button("5"))
# four = tk.Button(app, text="4", command=lambda: click_button("4"))
# three = tk.Button(app, text="3", command=lambda: click_button("3"))
# two = tk.Button(app, text="2", command=lambda: click_button("2"))
# one = tk.Button(app, text="1", command=lambda: click_button("1"))
# zero = tk.Button(app, text="0", command=lambda: click_button("0"))
# cross = tk.Button(app, text="x", command=lambda: click_button("x"))  # Backspace functionality added
# div = tk.Button(app, text="/", command=lambda: click_button("/"))
# mul = tk.Button(app, text="*", command=lambda: click_button("*"))
# sub = tk.Button(app, text="-", command=lambda: click_button("-"))
# add = tk.Button(app, text="+", command=lambda: click_button("+"))
# equal = tk.Button(app, text="=", command=lambda: click_button("="))
# ads = tk.Button(app, text="+/-", command=lambda: click_button("-"))
# dot = tk.Button(app, text=".", command=lambda: click_button("."))

# # Grid placement
# cross.grid(row=1, column=3, ipadx=10, ipady=10)
# div.grid(row=2, column=3, ipadx=10, ipady=10)

# seven.grid(row=3, column=0, ipadx=10, ipady=10)
# eight.grid(row=3, column=1, ipadx=10, ipady=10)
# nine.grid(row=3, column=2, ipadx=10, ipady=10)
# mul.grid(row=3, column=3, ipadx=10, ipady=10)

# four.grid(row=4, column=0, ipadx=10, ipady=10)
# five.grid(row=4, column=1, ipadx=10, ipady=10)
# six.grid(row=4, column=2, ipadx=10, ipady=10)
# sub.grid(row=4, column=3, ipadx=10, ipady=10)

# one.grid(row=5, column=0, ipadx=10, ipady=10)
# two.grid(row=5, column=1, ipadx=10, ipady=10)
# three.grid(row=5, column=2, ipadx=10, ipady=10)
# add.grid(row=5, column=3, ipadx=10, ipady=10)

# ads.grid(row=6, column=0, ipadx=10, ipady=10)
# zero.grid(row=6, column=1, ipadx=10, ipady=10)
# dot.grid(row=6, column=2, ipadx=10, ipady=10)
# equal.grid(row=6, column=3, ipadx=10, ipady=10)

# app.mainloop()
