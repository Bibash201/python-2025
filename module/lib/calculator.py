def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div():
    division=10/2
    return division


# Program to create a right triangle
def traingle():
    rows = int(input("Enter the number of rows for the triangle: "))
    
    for i in range(1, rows + 1):
       output=print("*" * i)
    return output    


# program to test elligible to vote or note
def test():
    age=int(input("enter your age:"))
    if age>=18:
        output=print(f"elligable to vote. Your age is {age}.")
        return output
    else:
        output=print(f"Notelligable to vote. Your age is {age}.")
        return output


  