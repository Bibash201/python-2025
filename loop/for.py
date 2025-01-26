# for num in range (1,11):
#     print("\n")
#     for i in range (1,11):
      
#         print(f"{num}x{i}={num*i}")

        
# rows = int(input("Enter the number of rows: "))

# # Loop to print the triangle
# for i in range(1, rows + 1):
#     print("*" * i)


# rows = int(input("Enter the number of rows: "))

# # Loop to print the triangle
# for i in range(1, rows + 1):
#     print("*" * i)


# data=['ram','shyam']
# for name in data:
#     print(name)


# for x in range (1,10):
#     print(x)

# for x in range (10,0,-1):
#     print(x)


# numbers=[
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15]
# ]
# for numbers in range(1,6):
#     print(numbers)
# for numbers in range (6,11):
#     print(numbers)
# for numbers in range(11,16):
#     print(numbers)
# //////same print
# for number in numbers:
#    print(number)


# numbers = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15]
# ]

# for row in numbers:
#     for num in row:
#         print(num)


# /////////////multipication
# //single multiple table
# num = int(input("Enter a number to print its multiplication table: "))
# for i in range(1, 11): 
#     print(f"{num} x {i} = {num * i}")

# //all multiple table from 1 to 10
# for num in range(1, 11): 
#     print(f"\nMultiplication Table for {num}:")  
#     for i in range(1, 11):  
#         print(f"{num} x {i} = {num * i}") 



# Write a program to calculate the sum of all numbers from 1 to 20 using a for loop.
# Calculate the sum of numbers from 1 to 20
sum_of_numbers = sum(range(1, 21))

# Display the result
print("The sum of numbers from 1 to 20 is:", sum_of_numbers)




# program to generate s marks detail?
# num=int(input("enter number of students"))
# student_markss=[]
# start=1
# while start<=num:
#     print(f"=====student{start}====")
#     nep=int(input('enter nep marks:'))
#     eng=int(input('enter eng marks:'))
#     helth=int(input('enter helth marks:'))
#     soc=int(input('enter soc marks:'))
#     math=int(input('enter math marks:'))
#     total=nep+eng+helth+soc+math
#     student_markss.append(total)
    

#     start+=1
# print("sn\ttotal marks\t percentage\t grade")
# x=1
# for mark in student_markss:
#     per=mark/5
#     grade=""
#     if per>=80:
#         grade="grade A" 
#     elif per>=60:
#         grade="grade b"
#     elif per>=40:
#         grade="grade c"
#     else:
#         grade="grade d"
#     print(f"{x}\t {mark}\t\t{per}\t\t{grade}\n")
 
#     x+=1


    

num=int(input("enter number of products"))
products=[]
start=1
while start<=num:
    print(f"=====product{start}====")
    price=int(input("enter price"))
    quentity=int(input("enter quentity"))
   
    total=price*quentity
    products.append(total)
    

    start+=1
print("sn\tproduct_price\t quentity\t total")
x=1
for sn in products:

      print(f"{x}\t{total}\t\t{quentity}\t \t{total}")
    
 
      x+=1

