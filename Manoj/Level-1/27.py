# 12.	Find number of days in a month

year = int(input("Enter the year to check : "))
month = int(input("Enter the month (1-12) : "))

if month in [1, 3, 5, 7, 8, 10, 12]:
  days = 31
  print(f"Number of Days : {days}")
elif month in [4, 6, 9, 11]:
  days = 30
  print(f"Number of days : {days}")
elif month==2:
  if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        days = 29
        print(f"Number of days : {days}")
  else:
        days = 28
        print(f"Number of days : {days}")
 
else:
    print("Invalid Input")