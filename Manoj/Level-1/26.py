# 11.	Check if year is century year and leap year

year = int(input("Enter the year to check : "))

if(year % 400  == 0):
  print("It is a leap year and a Century")
elif(year % 4 == 0 and year % 100 != 0):
  print("It is a leap year and not a Century")
else:
  print("It is neither a leap year nor a Century")