# Write a Python program to get next day of a given date using if-elif-else 
year = int(input("Input a year: "))

if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

while(True):
    month = int(input("Input a month [1-12]: "))
    if(month>12 or month<1):
        print("please enter in the range")
    else:
        break

if month in (1, 3, 5, 7, 8, 10, 12):
    month_len = 31
elif month == 2:
    if leap_year:
        month_len = 29
    else:
        month_len = 28
else:
    month_len = 30



while(True):
    day = int(input("Input a day [1-31]: "))
    if(day>31 or day<1):
        print("please enter in the range")
    else:
        break

if day < month_len:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))

