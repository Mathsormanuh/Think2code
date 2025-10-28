year=int(input("Enter the year: "))
if (year%400==0):
    print(f"{year} is a century year and leap year.")
elif (year%100==0):
    print(f"{year} is a century year and not a leap year.")
elif (year%4==0):
    print(f"{year} is not a century year but a leap year.")
else:
    print(f"{year} is not a century year and not a leap year.")