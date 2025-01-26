# x="1"
# print(type(x))
# integer type canot start with 0
# x=12
# print(type(x))


# float
# x=1.023
# print(type(x))

# Boolean(1st cap)
# x =True

# math
# a=45+67j
# print(type(a))
# print(a.real)
# print(a.img)

# price =102.1245
# print(f"(price:.2f)")

# type casting
# a ="2"
# print(type(a))
# a =int(a)
# print(type(a))

# a =input("enter a:")
# b =input("enter b:")

# print(a+b)


# name ='bibash'
# print(id(name))
# print(name[2])
# print(dir(name))


# a=65
# print (ord('a'))
# print(chr(65))

# + bata 0 bata negative bata aya 1 bata
# course ="we r learning python"
# print(course.upper())
# print(course.capitalize())
# print(course.title())
# print(dir(course))
# print(course[:])
# print(course[:2])
# print(course[2:])
# print(course[:-1])
# print(course[:])

# first =input("enter firsrname:")
# sec =input("enter secname:")
# third =input("enter thirdname:")
# print(first.capitalize(), sec.capitalize(), third.capitalize())


# program enter five sub marke and calcualte the total and Percentage
# a =int(input("enter mark of science"))
# b =int(input("enter mark of soc "))
# c =int(input("enter mark oif nep"))
# d =int(input("enter mark of eng"))
# e =int(input("enter mark of helth"))

# total =a+b+c+d+e
# percentage=int(total/500)*100
# print(f"total mark obtained: {total}")
# print(f"percentage: {percentage}%")

# list

# data =['ram','shyam','gita']
# print(data[0])



# data =['ram','shyam','gita']
# data[2]='kale'
# print(data)


# data=[]
# data.append('ram')
# data.append('gita')
# print(data)

# # clear list
# data.clear()
# print(data)

# insert
# data = []
# data.append('ram')
# data.append('gita')
# print(data)  
# data.insert(2, data[0])
# print(data) 

#count 
# ram_count = data.count('ram')
# print(f"Occurrences of 'ram': {ram_count}")

# index
# gita_index=data.index('gita')
# print(f"index of gita is {gita_index}")

# remove
# data=['ram','din','rita']
# data.remove('din')
# print(data)

# reverse
# data.reverse()
# print(data)

# sort
# data.sort()
# print(data)

# extend
# data.extend('gita')
# print(data)

# pop
# data=[1,2,3]
# # removing data of index 2
# data.pop(2)
# print(data)

# data=['ram','shyam']
# removing data of index 2
# data.pop()
# print(data)
# data1 =data.copy()
# print(data)

# data=[
#     ['ram','shyam'],
#     ['ramm','sshyam'],
# ]
# print(data[1][1])



#1. program to convert it in doller?
# rs=int(input("enter rupees"))
# amount=rs/128
# print(f"the dollor value of rs {rs} u enter is {amount} doller")


#2. program to enter paisa and convert it into rs?
# paisa=int(input("enter paisa"))
# rupees=paisa/100
# print(f"the value of paisa {paisa} u enter is {rupees} rupees")


#3. python program to check it is odd or even?
# a = int(input("Enter any value: "))
# if a % 2 == 0:
#     print("The number you entered is even")
# else:
#     print("The number you entered is odd")



#4. python program to enter any alphabet and check if it is vowel or consonent?
# alphabet = input("Enter any alphabet: ").lower()  
# if alphabet.isalpha() and len(alphabet) == 1:
#     if alphabet in 'aeiou':
#         print(f"The alphabet '{alphabet}' is a vowel.")
#     else:
#         print(f"The alphabet '{alphabet}' is a consonant.")
# else:
#     print("Invalid input! Please enter a single alphabet.")


#5. python program to enter number and check if it is positive or negative?
# number =int(input("enter any number u want to check:"))
# if number > 0:
#     print(f"{number} is positive.")
# elif number < 0:
#     print(f"{number} is negative.")
# else:
#     print("The number is zero.")


alphabet = input("Enter any alphabet: ").lower()  
if alphabet.isalpha() and len(alphabet) == 1:
    if alphabet in 'aeiou':
        print(f"The alphabet '{alphabet}' is a vowel.")
    else:
        print(f"The alphabet '{alphabet}' is a consonant.")
else:
    print("Invalid input! Please enter a single alphabet.")

