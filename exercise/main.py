# print("=========== Mobile Bazaar =========")
# print("Options: 1. MI (Rs:2000) 2. Samsung (Rs:5000) 3. Nokia (Rs:1500) 4. Lava (Rs:3000)")

# mi_price = samsung_price = nokia_price = lava_price = 0  # Initialize prices to 0
# product_name = ""
# quantity = 0

# option = int(input("Enter your choice: "))

# if option == 1:
#     product_name = 'MI'
#     quantity = int(input("Enter the quantity: "))
#     mi_price = quantity * 2000
# elif option == 2:
#     product_name = 'Samsung'
#     quantity = int(input("Enter the quantity: "))
#     samsung_price = quantity * 5000
# elif option == 3:
#     product_name = 'Nokia'
#     quantity = int(input("Enter the quantity: "))
#     nokia_price = quantity * 1500
# elif option == 4:
#     product_name = 'Lava'
#     quantity = int(input("Enter the quantity: "))
#     lava_price = quantity * 3000
# else:
#     print("Invalid choice")
#     exit()


# print("==== Delivery Options ====")
# print("1. Home (Rs:1000) 2. Pick up (Free)")
# delivery_price = 0
# delivery_option = int(input("Enter your choice: "))

# if delivery_option == 1:
#     delivery_price = 1000
# elif delivery_option == 2:
#     delivery_price = 0
# else:
#     print("Invalid delivery option")
#     exit()


# print("==== Packing Options ====")
# print("1. Normal (Rs:1000) 2. Gift (Rs:200)")
# packing_price = 0
# packing_option = int(input("Enter your choice: "))

# if packing_option == 1:
#     packing_price = 1000
# elif packing_option == 2:
#     packing_price = 200
# else:
#     print("Invalid packing option")
#     exit()


# print("==== Location Options ====")
# print("1. Kathmandu (13% tax) 2. Bhaktapur (0% tax) 3. Lalitpur (0% tax)")
# location_option = int(input("Enter your choice: "))
# tax_amount = 0


# total = mi_price + samsung_price + nokia_price + lava_price

# if location_option == 1:
#     tax_amount = total * 0.13
# elif location_option==2: 
#     tax_amount = 0
# elif location_option==3: 
#     tax_amount = 0
# else:
#     print("Invalid location option")
#     exit()


# grand_total = total + delivery_price + packing_price + tax_amount


# print("/////////// INVOICE ///////////")
# print(f"Product Name: {product_name}")
# print(f"Quantity: {quantity}")
# print(f"Total Price: Rs.{total}")
# print(f"Delivery Price: Rs.{delivery_price}")
# print(f"Packing Price: Rs.{packing_price}")
# print(f"Tax Amount: Rs.{tax_amount}")
# print(f"Grand Total: Rs.{grand_total}")






# print("=========== Laptop Bazaar =========")
# print("Options: 1. Acer (Rs:2000) 2. Lenovo (Rs:5000) 3. Samsung (Rs:1500) 4. Mac (Rs:3000)")

# acer_price = lenovo_price = samsung_price = mac_price = 0 
# product_name = ""
# quantity = 0


# option = int(input("Enter your choice: "))

# if option == 1:
#     product_name = 'Acer'
#     quantity = int(input("Enter the quantity (1-10): "))
#     if 1 <= quantity <= 10:
#         acer_price = quantity * 2000
#     else:
#         print("Invalid quantity! Must be between 1 and 10.")
#         exit()
# elif option == 2:
#     product_name = 'Lenovo'
#     quantity = int(input("Enter the quantity (1-10): "))
#     if 1 <= quantity <= 10:
#         lenovo_price = quantity * 5000
#     else:
#         print("Invalid quantity! Must be between 1 and 10.")
#         exit()
# elif option == 3:
#     product_name = 'Samsung'
#     quantity = int(input("Enter the quantity (1-10): "))
#     if 1 <= quantity <= 10:
#         samsung_price = quantity * 1500
#     else:
#         print("Invalid quantity! Must be between 1 and 10.")
#         exit()
# elif option == 4:
#     product_name = 'Mac'
#     quantity = int(input("Enter the quantity (1-10): "))
#     if 1 <= quantity <= 10:
#         mac_price = quantity * 3000
#     else:
#         print("Invalid quantity! Must be between 1 and 10.")
#         exit()
# else:
#     print("Invalid choice")
#     exit()


# print("==== Delivery Options ====")
# print("1. Home (Rs:1000) 2. Pick up (Free)")
# delivery_price = 0
# delivery_option = int(input("Enter your choice: "))

# if delivery_option == 1:
#     delivery_price = 1000
# elif delivery_option == 2:
#     delivery_price = 0
# else:
#     print("Invalid delivery option")
#     exit()


# print("==== Packing Options ====")
# print("1. Normal (Rs:1000) 2. Gift (Rs:200)")
# packing_price = 0
# packing_option = int(input("Enter your choice: "))

# if packing_option == 1:
#     packing_price = 1000
# elif packing_option == 2:
#     packing_price = 200
# else:
#     print("Invalid packing option")
    


# print("==== Location Options ====")
# print("1. Kathmandu (13% tax) 2. Bhaktapur (0% tax) 3. Lalitpur (0% tax)")
# location_option = int(input("Enter your choice: "))
# tax_amount = 0


# total = acer_price + lenovo_price + samsung_price + mac_price

# if location_option == 1:
#     tax_amount = total * 0.13
# elif location_option in [2, 3]:  
#     tax_amount = 0
# else:
#     print("Invalid location option")
#     exit()


# grand_total = total + delivery_price + packing_price + tax_amount


# print("/////////// INVOICE ///////////")
# print(f"Product Name: {product_name}")
# print(f"Quantity: {quantity}")
# print(f"Total Price: Rs.{total}")
# print(f"Delivery Price: Rs.{delivery_price}")
# print(f"Packing Price: Rs.{packing_price}")
# print(f"Tax Amount: Rs.{tax_amount}")
# print(f"Grand Total: Rs.{grand_total}")


# program to check password and uname/////////////////

# userName=input("entrer uname:")
# password=input("entrer password:")
# if userName=="admin":
#     if password=="admin":
#         print("welcome to page")
#     else:
#         print("incorect password")
# else:
#     print("incorect uname")



age=int(input("enter ur age"))
if age>18 and age<40:
    if age>18 and age<25:
        print("u can eat only momo")
    elif age>25 and age<35:
        print("u can drink bear")
    elif age>35 and age<40:
        print("u can eat pizza")
        


else:
    print("u are child or overage")




