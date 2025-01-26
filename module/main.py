# import math
# print(dir(math))
# print(math.pi)
# print((math.pow(2,1)))

# import datetime
# print(dir(datetime))
# print(datetime.datetime.now())
# print(datetime.datetime.now().year)
# new_date=datetime.datetime(1993,5,10)
# today=datetime.datetime.now()
# print(today-new_date)
# date="2020-12-12"
# print(datetime.datetime.strptime(date,"%Y-%m-%d"))






# import datetime

# def calculate_time_to_birthday(birthday):
#     # Get today's date
#     today = datetime.date.today()
    
#     # Extract the year from today
#     current_year = today.year
    
#     # Replace the year of the birthday with the current year
#     next_birthday = birthday.replace(year=current_year)
    
#     # Check if the birthday this year has passed
#     if next_birthday < today:
#         # If passed, calculate for the next year
#         next_birthday = birthday.replace(year=current_year + 1)
    
#     # Calculate the difference between today and the next birthday
#     time_remaining = next_birthday - today
#     days_remaining = time_remaining.days
    
#     # Approximate months remaining
#     months_remaining = days_remaining // 30  # Assume 30 days per month for approximation
    
#     return days_remaining, months_remaining

# def main():
#     # Ask the user for their birth date
#     print("Enter your birthdate:")
#     year = int(input("Year (YYYY): "))
#     month = int(input("Month (MM): "))
#     day = int(input("Day (DD): "))
    
#     try:
#         # Create a date object for the birthday
#         birthday = datetime.date(year, month, day)
        
#         # Calculate days and months remaining
#         days, months = calculate_time_to_birthday(birthday)
        
#         # Display the result
#         print(f"Your next birthday is in {days} days (approximately {months} months).")
#     except ValueError as e:
#         print(f"Invalid date entered: {e}")

# if __name__ == "__main__":
#     main()




# import datetime
# b_date=input("enter date(yyyy-mm-d):")
# n_date=datetime.datetime.strptime(b_date,"%Y-%m-%d")
# today=datetime.datetime.now()
# if today>n_date:
#     day=today-n_date
#     print("your birthday date is",day.days,"days ago.")
# else:
#     day=n_date-today
#     print("your birthday date is in future",day.days,"days left.")


# makae rthis code as above so that when user enter any date show not expired job title and give massage you can apply in above job


# import datetime
# jobs = [
#     {'title': 'Python Developer', 'salary': 20000, 'exp_date': '2025-5-21'},
#     {'title': 'Java Developer', 'salary': 30000, 'exp_date': '2024-5-21'},
#     {'title': 'PHP Developer', 'salary': 40000, 'exp_date': '2025-5-21'},
#     {'title': 'Web Developer', 'salary': 50000, 'exp_date': '2022-6-21'},
# ]

# # Get the user's input date
# user_input = input("Enter a date (yyyy-mm-dd): ")

# try:
#     user_date = datetime.datetime.strptime(user_input, "%Y-%m-%d").date()
#     valid_jobs = []

#     # Check each job's expiration date
#     for job in jobs:
#         job_exp_date = datetime.datetime.strptime(job['exp_date'], "%Y-%m-%d").date()
#         if user_date <= job_exp_date:
#             valid_jobs.append(job)

#     # Display results
#     if valid_jobs:
#         print("You can apply for the following jobs:")
#         for job in valid_jobs:
#             print(f"- {job['title']} (Salary: {job['salary']}, Expiration Date: {job['exp_date']})")
#     else:
#         print("No jobs available to apply for.")

# except ValueError:
#     print("Invalid date format. Please enter the date in 'yyyy-mm-dd' format.")









# import datetime
# jobs = [
#     {'title': 'Python Developer', 'salary': 20000, 'exp_date': '2025-5-21'},
#     {'title': 'Java Developer', 'salary': 30000, 'exp_date': '2024-5-21'},
#     {'title': 'PHP Developer', 'salary': 40000, 'exp_date': '2025-5-21'},
#     {'title': 'Web Developer', 'salary': 50000, 'exp_date': '2022-6-21'},
# ]

# user_input = input("Enter a date (yyyy-mm-dd): ")
# user_date = datetime.datetime.strptime(user_input, "%Y-%m-%d")
# valid_jobs = []

# for job in jobs:
#     job_exp_date = datetime.datetime.strptime(job['exp_date'], "%Y-%m-%d")
#     if user_date <= job_exp_date:
#         valid_jobs.append(job)

# if valid_jobs:
#     print("You can apply for the following jobs:")
#     for job in valid_jobs:
#         print(f"- {job['title']} (Salary: {job['salary']}, Expiration Date: {job['exp_date']})")
# else:
#     print("No jobs available to apply for.")


# jobs =[
#     {'title':'python developer', 'salary':20000, 'exp_date':'2025-5-21'},
#     {'title':'java developer', 'salary':30000, 'exp_date':'2024-5-21'},
#     {'title':'php developer', 'salary':40000, 'exp_date':'2025-5-21'},
#     {'title':'web developer', 'salary':50000, 'exp_date':'2022-6-21'},
# ]

# import datetime

# for job in jobs:
#     job_exp_date = datetime.datetime.strptime(job['exp_date'], "%Y-%m-%d")
#     today = datetime.datetime.now()
#     if today>job_exp_date:
#         diff = today - job_exp_date
#         print(f"{job['title']} job is expired {diff.days} days ago")
#     else:
#         diff = job_exp_date - today
#         print(f"{job['title']} job is going to expire in {diff.days} days")






#//////////////// module lai import garera yo run garnu parxa->user=file name 
# import user   ///yo garda user.py run

# ////calculator file lai as cal_ma change
# import calculator as cal
# print (cal.add(5,5))


# from calculator import add, sub
# print(add(1,1))
# print(sub(6,5))


# ///calculatorko import sabai
# from calculator import *
# print(add(1,1))
# print(sub(3,1))
# print(mul(2,2))
# print(div())


# /////lib ko vitrako calculator
# from lib import calculator
# print(add(2,6))


# //////lib vitra ko sabai import
# from lib import *
# #  //calculator vitrako add
# print (calculator.add(2,3)) 
# print (calculator.div()) 
# print(student.get_all())
# calculator.traingle()
# calculator.test()

