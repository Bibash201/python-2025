
import re #//// for run regex import re must be import.....

# dis ='Iamram'
# patterns = '^[a-zA-Z]*$'
# if re.match(patterns,dis):
#     print('Match')
# else:
#     print('Not Match')



# //////////////[assword vallidation check]
# import re(aLREADY IMPORT)
# def check_password(password):
#     # Regular expression for password validation
#     pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!])[A-Za-z\d@#$%^&+=!]{8,}$'
#     if re.match(pattern, password):
#         return True
#     return False

# # Ask user for input
# password = input("Enter your password: ")

# # Check password validity
# if check_password(password):
#     print("Password is valid.")
# else:
#     print("Password is not valid. Ensure it meets all the criteria.")





# //////password validation check and if valid store passeord in auth.txt
password=input("enter your password:")
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!])[A-Za-z\d@#$%^&+=!]{8,}$'
if re.match(pattern,password):
    with open("regex/auth.txt", "a") as handle:  # Open file in append mode
        handle.write(f"password:{password}\n")
        print("matched saved")
        handle.close()
else:
     print('Not Match')


