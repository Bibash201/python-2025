# class Bank:
#     __name="SBI"
#     def getBank(self):# get method access, return type hunxa
#         return self.__name
#     def setBank(self,name):#retur type hunna
#         self.__name=name
# obj=Bank()
# obj.setBank("hdc")
# print(obj.getBank())



# class BankAccount:
#     __bankHolder = "Bibash"

#     def getBankAccount(self):
#         return self.__bankHolder

#     def setBankAccount(self, name):
#         self.__bankHolder = name
# # Creating an instance of BankAccount
# obj = BankAccount()
# obj.setBankAccount("Ram")
# print(obj.getBankAccount())

# setter//////////////////

# class Bank:
#     __name="SBI"
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,name):
#         self.__name=name
# obj=Bank()
# obj.name='test'
# print(obj.name)

# class Clz:
#     __name="ABC"
#     @property
#     def sname(self):
#         return self.__sname
#     @sname.setter
#     def sname(self,sname):
#         self.__sname=sname
# obj=Clz()
# obj.sname='Ram'
# print(obj.sname)
#description of code.........
# Key Features and Explanation:
# 1.Private Attribute:
# __name: A private class attribute with the value "ABC".
# This attribute is not accessible directly outside the class.
# 2.@property Decorator:
# The @property decorator is used to define a getter method for the sname property.
# It allows sname to be accessed like an attribute (e.g., obj.sname) while actually calling the sname method.
#3. @sname.setter Decorator:
# The @sname.setter decorator is used to define a setter method for the sname property.
# It allows sname to be assigned a value like an attribute (e.g., obj.sname = 'Ram'), while internally invoking the setter method to set the value.
# Dynamic Setting and Getting:
# You create an instance of the class Clz and assign a value to the sname property using the setter.
# Later, you retrieve the value using the getter and print it.
# Issues in the Code:
# Uninitialized Attribute:
# The private attribute __sname is not initialized in the class or its constructor (__init__). Trying to access obj.sname before setting it will result in an AttributeError.



#/////////////@staticmethod
# class Mobile:

#     @staticmethod   #classko obj garaunu pardaina //self rakhnu pardaina instance create garnu naaprekole
#     def info():
#         print("i am Bibash.")
# Mobile.info()



# class Products:
#     @staticmethod
#     def noodlees():
#         print("wai wai")
#     @staticmethod
#     def biscuits():
#         print("coconut")
# Products.noodlees()
# Products.biscuits()



#///////////////classmethod
    # 1.Takes the class itself (cls) as its first parameter.
    # 2.Can access and modify class attributes or call other class methods.
# class Products:
#     @classmethod
#     def noodles(cls):
#         print("Wai Wai")
#     @classmethod
#     def biscuits(cls):
#         print("Coconut")
# Products.noodles()  # Call the noodles method using the class
# Products.biscuits()  # Call the biscuits method using the class



class Company:
    @classmethod
    def cg(cls,work):
        return work
print(Company.cg("beer"))