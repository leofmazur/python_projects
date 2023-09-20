print("Welcome to the Leap Year Finder!")
year = float(input("Which year do you want to check out? "))

year_check1 = year % 4
year_check2 = year % 100
year_check3 = year % 400

if year_check1 != 0:
    print("Not a leap Year!")
else:
    if year_check2 == 0 and year_check3 != 0:
        print("Not a leap Year!")
    else:
        print("Leap Year!")

# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#         return True
#   else:
#     return False
    
# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if month > 12 or month < 1:
#     return "Invalid month entered."
#   if month == 2 and is_leap(year):
#     return 29
#   return month_days[month - 1]