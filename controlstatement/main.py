# x=6
# y=8
# if x>y:
#     print("x greater")
# else:
#     print("y is greater")


# x=8
# y=8
# if x>y:
#     print("x greater")
# elif x==y:
#     print("equal")
# else:
#     print("y is greater")



# progrem to check greater
# num1=int(input("enter num1:"))
# num2=int(input("enter num2:"))
# num3=int(input("enter num3:"))
# if num1>num2>num3:
#     print('num1 greater')
# elif num2>num3>num1:
#     print("num2 greater")
# else:
#     print("num3 greater")



# check even or odd
# a =int(input("enter numver:"))
# if a%2==0:
#     print("a ig even")
# else:
#     print("a is odd")



# to check person is eligible to vote or not
# age=int(input("enter age of person:"))
# if age>=18:
#     print("sligible to vote")
# else:
#     print("not elligible to vote")

# username="admin"
# upw="password"
# uname=input("enter u name:")
# pw=input("enter pw:")
# if username==uname and upw==pw:
#     print(f"welcome {username}")
# else:
#     print("invilid uname and pw")
     


# ////////marks of student and fine per grade
# science = int(input("Enter marks obtained in Science: "))
# np = int(input("Enter marks obtained in Nepali: "))
# soc = int(input("Enter marks obtained in Social Studies: "))
# eng = int(input("Enter marks obtained in English: "))
# hel = int(input("Enter marks obtained in Health: "))


# total = science + np + soc + eng + hel
# max_marks = 500  
# per = (total / max_marks) * 100


# print(f"\nTotal Marks = {total}")
# print(f"Percentage = {per:.2f}%")


# if science>=35 and np>=35 and soc>=35 and eng>=35 and hel>=35 and per>=85:
#     print("grade=A")
# elif science>=35 and np>=35 and soc>=35 and eng>=35 and hel>=35 and per>=60 and per<85:
#     print("grade=B")
# elif science>=35 and np>=35 and soc>=35 and eng>=35 and hel>=35 and per>=45 and per<60:
#     print("grade=c")
# elif science>=35 and np>=35 and soc>=35 and eng>=35 and hel>=35 and per>=35 and per<45:
#     print("grade=D")
# else:
#     print("ng")



# ///////atm process
# balance = 1000
# keptPin = 1234
# print("Insert your card")
# pin = int(input("Enter your pin: "))

# if pin == keptPin:
#     print("Welcome! Choose your option.")
#     print("Enter 1 for blnc inquiry:")
#     print("Enter 2 for withdraw:")

#     option = int(input("Enter option: "))
#     if option == 1:
#         print(f"Your current balance is: {balance}")
#     elif option == 2: 
#         amount = int(input("Enter amount you want to withdraw: "))
#         if amount <= balance:
#             balance -= amount
#             print("Withdraw successful!")
#             print(f"Your remaining balance is: {balance}")
#         else:
#             print("Insufficient balance.")
#     else:
#         print("Invalid option.")  
# else:
#     print("Incorrect PIN.")




# /////////////enter threee number and print in decending order 
num1=int(input("enter first number:"))
num2=int(input("enter sec number:"))
num3=int(input("enter third number:"))
if num1>num2>num3:
    print(f"{num1}, {num2}, {num3}")
elif num2>num3>num1:
    print(f"{num2}, {num3}, {num1}")
elif num2>num1>num3:
    print(f"{num2}, {num1}, {num3}")
elif num3>num1>num2:
    print(f"{num3}, {num1}, {num2}")
elif num3>num2>num1:
    print(f"{num3}, {num2}, {num1}")
# else:
#     print("")










       


    

