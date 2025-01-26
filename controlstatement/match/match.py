# language="nepali"
# match language:
#     case "nepali":
#       print("nameste")
#     case  "english":
#       print("hello")
#     case _:
#       print("Invalid")


# //'// program to enter any operator and two lnumbers and perform the operator

# operator = input("Enter an operator (+, -, *, /): ")
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# # Perform the operation using match-case
# match operator:
#     case "+":
#         result = num1 + num2
#     case "-":
#         result = num1 - num2
#     case "*":
#         result = num1 * num2
#     case "/":
#         if num2 != 0:
#             result = num1 / num2
#         else:
#             result = "Error! Division by zero is not allowed."
#     case _:
#         result = "Invalid operator!"

# print("Result:", result)


#to enter three number and print assending order

# order="dessending"
# num1=int(input("enter number1:")) 
# num2=int(input("enter number2:"))
# num3=int(input("enter number3:"))
# match order:
#     case "dessending":
#         if num1>num2>num3:
#             print(f"{num1}, {num2}, {num3}")
#         elif num2>num3>num1:
#             print(f"{num2}, {num3}, {num1}")
#         elif num3>num1>num2:
#              print(f"{num3}, {num1}, {num2}")
#         elif num3>num2>num1:
#              print(f"{num3}, {num2}, {num1}")
#         elif num1>num3>num2:
#              print(f"{num1}, {num3}, {num2}")
#         elif num2>num1>num3:
#              print(f"{num2}, {num1}, {num3}")   
#     case _:
#         print("invalid order")

# order="assending"
# num1=int(input("enter number1:")) 
# num2=int(input("enter number2:"))
# num3=int(input("enter number3:"))
# match order:
#       case "assending":
#         print(f"an assending order of number you enter {num1}, {num2}, {num3}:")
#         if num1>num2>num3:
#             print(f"{num3}, {num2}, {num1}")
#         elif num2>num3>num1:
#             print(f"{num1}, {num3}, {num2}")
#         elif num3>num1>num2:
#              print(f"{num2}, {num1}, {num3}")
#         elif num3>num2>num1:
#              print(f"{num1}, {num2}, {num3}")
#         elif num1>num3>num2:
#              print(f"{num2}, {num3}, {num1}")
#         elif num2>num1>num3:
#              print(f"{num3}, {num1}, {num2}") 
       
#         else:
#             print("")

#       case _:
#         print("invalid order")


username=input("user name:")
password=input("enter password:")
if username=="admin":
    if password=="admin":
        print("wellcome.....")
    else:
        print("incorrect password")
elif username=="ram":
    if password=="ram":
        print("wellcome.....")
    else:
        print("incorrect password")


else:
    print("user name incotrect")




