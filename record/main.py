# handle=open("record/db.txt","w")
# handle.write("hello,update\n")
# handle.write("hello,test\n")
# handle.close()


# name=input("enter name:")
# email=input("enter mail:")
# address=input("enter address:")
# handle=open("record/practice.txt","w")
# handle.write(f"name:{name}\n")
# handle.write(f"address:{address}\n")
# handle.write(f"email:{email}\n")
# handle.close()

# obj=open("record/practice.txt","r")
# print(obj.read())




# print("==================Mobile Bazar==============")
# print("1. Mi(Rs:20000) 2. Samsung(Rs:30000) 3. Iphone(Rs:50000)")

# mi_price =0
# samsung_price =0
# iphone_price =0
# product_name=""
# quantity = 0
# option = int(input("Enter your choice: "))
# if option==1:
#     product_name = "Mi"
#     quantity = int(input("Enter the quantity: "))
#     mi_price = 20000 * quantity

# elif option==2:
#     product_name = "Samsung"
#     quantity = int(input("Enter the quantity: "))
#     samsung_price = 30000 * quantity

# elif option==3:
#     product_name = "Iphone"
#     quantity = int(input("Enter the quantity: "))
#     iphone_price = 50000 * quantity
# else:
#     print("Invalid choice")

# print("Delivey Option")
# print("1. Home Delivery(Rs:1000) 2. Pick up(Free)")
# delivery_price =0
# delivery_option = int(input("Enter your choice: "))
# if delivery_option==1:
#     delivery_price = 1000


# print("Packing: 1. Normal(Rs:1000) 2. Gift Packing(Rs:5000)")
# packing_price =0
# packing_option = int(input("Enter your choice: "))
# if packing_option==1:
#     packing_price = 1000
# elif packing_option==2:
#     packing_price = 5000

# print("Location: 1.KTM(13%) 2. Lalitpur(0%) 3. Bhaktapur(0%)")
# tax_amount =0
# location_option = int(input("Enter your choice: "))
# total = mi_price + samsung_price + iphone_price
# if location_option==1:
#     tax_amount = total * 0.13

# grand_total = total + delivery_price + packing_price + tax_amount
# print("======== Invoice =========")
# print(f"Product Name: {product_name}")
# print(f"Quantity: {quantity}")
# print(f"Total: {total}")
# print(f"Delivery Price: {delivery_price}")
# print(f"Packing Price: {packing_price}")
# print(f"Tax Amount: {tax_amount}")
# print(f"Grand Total: {grand_total}")



# handle=open("record/mbl.txt","w")

# handle.write(f"product_name:{product_name}\n")
# handle.write(f"quentity:{quantity}\n")
# handle.write(f"total:{total}\n")
# handle.write(f"delivery_option:{delivery_option}\n")
# handle.write(f"Delivery Price: {delivery_price}\n")
# handle.write("Packing: 1. Normal(Rs:1000) 2. Gift Packing(Rs:5000)\n")
# handle.write(f"packing_option:{packing_option}\n")
# handle.write(f"Packing Price: {packing_price}\n")
# handle.write("Location: 1.KTM(13%) 2. Lalitpur(0%) 3. Bhaktapur(0%)\n")
# handle.write(f"location_option:{location_option}\n")
# handle.write(f"Tax Amount: {tax_amount}\n")
# handle.write(f"Grand Total: {grand_total}\n")



# /////////program that take register from user, store it to user.txt and test login if success access book list to view from book.txt
# handle=open("record/user.txt","w")
# handle.write("==========register=========\n")
# print("==========register=========")
# uname=input("Enter username:")
# upassword=input("Enter password:")
# handle.write(f"username:{uname},password:{upassword}\n")
# handle.write("==========login=========\n")
# print("==========login=========")
# username=input("Enter username:")
# password=input("Enter password:")
# if username==uname:
#     if password==upassword:
#         print("sucess login")
#         handle.write("sucess login")
#         handle=open("record/book.txt","w")
#         handle.write("ramayan\n")
#         handle.write("munamadan\n")
#         handle.write("sostik\n")
#         print("======book_list=====")
#         print("ramayan")
#         print("munamadan")
#         print("sostik")

#     else:
#         print("invalid password")
#         handle.write("wromg password")
# else:
#     print("wrong username")
#     handle.write("invalid username")
# handle.close()

# ///function
# handle=open("record/user.txt","w")
# handle.write("==========register=========\n")
# print("==========register=========")
# uname=input("Enter username:")
# upassword=input("Enter password:")
# handle.write(f"username:{uname},password:{upassword}\n")
# handle.write("==========login=========\n")
# print("==========login=========")
# username=input("Enter username:")
# password=input("Enter password:")
# def authorization():
#  if username==uname:
#     if password==upassword:
#         print("sucess login")
#         handle.write("sucess login")
#         handle=open("record/book.txt","w")
#         handle.write("ramayan\n")
#         handle.write("munamadan\n")
#         handle.write("sostik\n")
#         print("======book_list=====")
#         print("ramayan")
#         print("munamadan")
#         print("sostik")

#     else:
#         print("invalid password")
#         handle.write("wromg password")
#  else:
#     print("wrong username")
#     handle.write("invalid username")


# # /////The construct if __name__ == "__main__": is a common Python idiom used to control the execution of code when a script is run directly, versus when it is imported as a module in another script.
# if __name__ == "__main__":
#  authorization()

# handle.close()




# def add(x,y):
#  return(x+y)
#  print(add(2,5))
# def sub(x,y,z):
#     return(x-y-z)
# print(sub(8,2,3))
# def multiply():
#     x=5
#     y=10
#     z=x*y
#     return(z)
# print(multiply())


