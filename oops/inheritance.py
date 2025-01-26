# class Dell:
#     def  name(self,name):
#         print(f"brand {name}")

# class Mac:
#     def  name(self,name):
#         print(f"brand {name}")

# obj=Dell()
# obj.name("Dell")
# obj2=Mac()
# obj.name("Mac")


# class Laptop:
#     def brand(self,name):
#         print(f"Brand name is {name}")
# class Dell(Laptop):
#     pass
# class Mac(Laptop):
#     pass
# obj=Dell()
# obj.brand("dell")
# obj2=Mac()
# obj2.brand("Mac")


# class Mobile:
#     def brand(self,name):
#         model="samsung"
#         price=10000
#         print(f"Brand name is {name}")
#         print(f"price is {price}")
# class Samsung(Mobile):
#     pass
# class Mac(Mobile):
#     pass
# obj=Mobile()
# obj.brand("samsung")



#  donder methoid (self run)
class Laptop:
    def __init__(self,name):
        print("laptop onj created",name) 


    def __del__(self):
         print("laptop onj destroyed") 


obj=Laptop("dell")


class Laptop:
    name="samsung"


    def __str__(self):
         return self,name


obj=Laptop("dell")




# super(). parent ko constroctur call when one class badi class vya j name x tyhe

#  total nikalda self le kam gardaina so class,total+=1

# class vitra variable one underscore vya eg _name=protected and __name=private class