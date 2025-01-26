# variables rule:
# 1.start with letter or underscore
#   x=7
# 2.should not start with number  
# 3.should not contain Space
# 4.should not special character except under
#   user_name:snake case-> function
#   userName: canel case ->varable
#   UserName: pascal name->class 

# name ="bibash"
# address="kws"
# age=3
# print("my name is {}. i am from {}. i am {} years old".format(name,address,age))

name =input("enter name:")
address =input("enter address:")
age =input("enter age:")
# print(f"my name is {name}. i am from {address}. i am {age} years old")
# print(name,address,age)
print("my name is", name)
