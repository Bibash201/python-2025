# def total(numbers):
#     x = 0
#     for a in numbers:
#         x += a
#     print(x)

# total(1, 2, 3, 4, 5,6,7)

# def display_multiplication_table(number):
#     """Prints the multiplication table for the given number."""
#     for i in range(1, 11):  # Loop from 1 to 10
#         print(f"{number} x {i} = {number * i}")

# # Take input from the user
# user_input = int(input("Enter a number to display its multiplication table: "))

# # Call the user-defined function
# display_multiplication_table(user_input)





# //////to print multipication table of user given number
# def mul(numbers):
#     for i in range(1,11):
#         print(f"{numbers}x{i}={numbers*i}")

# input_number=int(input("enter number u want to dispaly multipication table:"))
# mul(input_number)



# def calculate_sum(numbers):
#     """Calculates the sum of a list of numbers."""
#     total = 0
#     for num in numbers:
#         total += num
#     return total

# # Take input from the user
# user_input = input("Enter numbers separated by spaces: ")

# # Convert the input string into a list of integers
# numbers = list(map(int, user_input.split()))

# # Call the function and print the result
# result = calculate_sum(numbers)
# print(f"The sum of the entered numbers is: {result}")




# /////////// WAP to find largest number from list
# def find_largest(numbers):
#     """Prints the largest number in a list."""
#     largest = numbers[0]  # Assume the first number is the largest
#     for num in numbers:
#         if num > largest:  # Compare each number with the current largest
#             largest = num
#     print(f"The largest number in the list is: {largest}")

# # Take input from the user
# user_input = input("Enter numbers separated by spaces: ")

# # Convert the input string into a list of integers
# numbers = list(map(int, user_input.split()))

# # Call the function
# find_largest(numbers)




# ////////find sum from nested list .
# data = [
#     [34, 56, 87, 65, 56],
#     [56, 67, 78, 89, 90],
# ]
# def find_sum(data):
#     """Calculates and prints the sum of all values in a nested list."""
#     total_sum = 0  # Initialize sum to 0
#     for row in data:  # Iterate through each sublist in the main list
#         for value in row:  # Iterate through each value in the sublist
#             total_sum += value  # Add the value to the total sum
#     print(f"The total sum of values is: {total_sum}")
    
# find_sum(data)



# def add(x,y):
#     return x+y
# add(2,9)

# def total(a,b):
#     print(add(a,b))

# total(10,20)


# def take_mark():
#     pass
# # five subject marks return


# def total():
#     # calculate total marks
#     pass 

# def percentage():
#     # calculate percentage
#     pass

# def display():
#     # display result
#     pass
# def inputmarks():
#  math=int(input("enter math marks:"))
#  science=int(input("enter math science:"))
#  social=int(input("enter social marks:"))
#  nepali=int(input("enter nepai marks:"))
#  def total():
#   total_marks=math+science+social+nepali
#   return total_marks
#  total_marks=total()


# def inputmarks():
#     math = int(input("Enter math marks: "))
#     science = int(input("Enter science marks: "))
#     social = int(input("Enter social marks: "))
#     nepali = int(input("Enter nepali marks: "))

 
#     def total():
#         total_marks = math + science + social + nepali
#         return total_marks
#     total_marks = total()
    
   
#     percentage = (total_marks / 400) * 100
    
   
#     if percentage >= 90:
#         grade = 'A+'
#     elif percentage >= 80:
#         grade = 'A'
#     elif percentage >= 70:
#         grade = 'B+'
#     elif percentage >= 60:
#         grade = 'B'
#     elif percentage >= 50:
#         grade = 'C+'
#     elif percentage >= 40:
#         grade = 'C'
#     else:
#         grade = 'F'

#     # Print results
#     print(f"Total Marks: {total_marks}")
#     print(f"Percentage:{percentage:.2f}%")
#     print(f"Grade: {grade}")

#     if math>=35 and social>=35 and science>=35 and nepali>=35:
#         print("your result is: PASSED")
#     else:
#         print("Your result is: FAILL")

# inputmarks()




# def inputmark():
#     math=int(input("enter math marks:"))
#     science=int(input("enter science marks:"))
#     english=int(input("enter english"))
#     def total():
#        total_marks=0
#        total_marks= math + science + english
#        return total_marks
#        total_marks=total()
#        print(f"total marks:{total_marks}")
#        def percentege():
#          per=(total_marks/3)
#          return per
# //The function returns the calculated value of per.
        #  per=percentege()
#       ///Call the percentege function and assign its return value to per.
# The function percentege is called, and its result is stored in the variable per.
# This line will throw an error if total_marks is undefined.

        #  print(f"percentage:{per}")
        #  percentege()
#        //Call the percentege function again.
# The function is called a second time, but its return value is not assigned or used.
# This line has no effect on the output, though it still performs the calculation.
# inputmark()


# def inputmark():
#     math=int(input("enter math marks:"))
#     science=int(input("enter science marks:"))
#     english=int(input("enter english:"))
#     def total():
#        total_marks= math + science + english
#        return total_marks
#     total_marks=total()
#     print(f"total marks:{total_marks}")
#     def percentage():
#         per=total_marks/3
#         return per
#     per=percentage()
#     print(f"total percentage:{per}")
#     percentage()
# inputmark()




