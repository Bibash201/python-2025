# oop:
#   is a object oriented programing language.structure show
# class:
#   is a blueprient of object
# object:
#    is an instance of class



# yo variable, function lai rap garera rakhya class bhaninxa
# variable
#x=10  
# function
#def test():
#     print("hello")
# test()



# class Car:
#      price=1000 #property/variable

#      def model(self): ##method/function
#         print("this is model")
#instance of class
# a=Car() #object of class
# print(a.price) #define and call
# a.model()


# class Bird:
#     name="parrot"

#     def colour(self):
#         a=Bird()
#         print(f"{a.name} is green.")
#     def add(self,x,y):
#         print(x+y)          
# #instance of class
# b=Bird()
# print(b.name)
# b.colour()
# b.add(5,3)

# class Calculator:
#     def add(self,x,y):
#         print(x+y)
#     def sub(self):
#         a=int(input("Enter first number:"))
#         b=int(input("Enter sec number:"))
#         return a-b
    
# t=Calculator()
# t.add(5,6)
# print(t.sub())


#program for calculator using class?
# class Calculatoir:
#     def __init__(self):
#         self.a=int(input("enter first num:"))
#         self.b=int(input("enter sec number:"))

#     def add(self): 
#         add=self.a+self.b
#         print(f"sum of {self.a} and {self.b} is",add)       
#     def sub(self):
#         sub=self.a-self.b
#         print(f"difference of {self.a} and {self.b} is",sub)
#     def div(self):
#         return (self.a/self.b)


# x=Calculatoir()
# print("1:add \n2:sub \n3:div")
# option=int(input("enter your option:"))
# if option==1:
#     x.add()
# elif option==2:
#     x.sub()
# elif option==3:
#     print(f"result:",x.div())
# else:
#     print("invalid option....")




# class Calculator:
#     def __init__(self):
#         #Key Points About __init__:
# # It is automatically called when an object is created.
# # It can take additional arguments (like a and b) if needed.
# # It ensures the class is ready to use by setting up the initial state of the object.
#         # Initialize and take inputs for `a` and `b` when creating an object
#         self.a = int(input("Enter first number: "))
#         self.b = int(input("Enter second number: "))
#         #The values entered by the user are stored in the instance variables self.a and self.b

#     def add(self):
#         result = self.a + self.b
#         print(f"The sum is: {result}")

#     def sub(self):
#         result = self.a - self.b
#         print(f"The difference is: {result}")

# # Create the calculator object
# x = Calculator()

# # Provide an option to the user to select an operation
# option = int(input("Choose an option:\n1: Add\n2: Subtract\n"))

# if option == 1:
#     x.add()
# elif option == 2:
#     x.sub()
# else:
#     print("Invalid option!")

hande=open("ram.txt")
class Calculator:
    def __init__(self):
        self.a=int(input("enter first number:"))
        self.b=int(input("enter second number:"))
    def add(self):
        add=self.a+self.b
        print(f"addition of {self.a}+{self.b}" "=",add)
    def sub(self):
        return(self.a-self.b)
x=Calculator()
print("1:add \n2:sub")
option=int(input("enter option:"))
if option==1:
 x.add()
elif option==2:
 print(f"the difference is",x.sub())
else:
   print("invilid option....")


    
   
     
     
     



