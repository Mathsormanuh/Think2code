# 1.	Check if number is even or odd

'''a = int(input("Enter the number of a : "))

if(a%2==0):
  print("The number is even")

else:
  print("The number is odd")'''

# 2.	Find largest of three numbers

'''a = int(input("Enter the number of a : "))
b = int(input("Enter the number of b : "))
c = int(input("Enter the number of c : "))

if(a>b and a>c):
  print("a is greatest")
elif(b>a and b>c):
  print("b is greatest")
else:
  print("c is greatest")'''

# 3.	Check leap year

'''year = int(input("Enter the year to check : "))

if(year % 4 == 0 and year % 100 != 0):
  print("It is a leap year")
elif(year % 400  == 0):
  print("It is a leap year")
else:
  print("It is not a leap year")'''

# 4.	Check if character is vowel or consonant

'''a = (input("Enter the year to check : "))

if(a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u'):
  print("Vowel")
else:
  print("Consonant")'''

# 5.	Check if student passed or failed

'''mark = int(input("Enter the student mark : "))

if(mark < 50):
  print("Fail")
else:
  print("Pass")'''

# 6.	Calculate grade based on marks

'''marks = int(input("Enter the student marks : "))

if marks >= 90:
  grade = 'A'
elif marks >= 80:
  grade = 'B'
elif marks >= 70:
  grade = 'C'
elif marks >= 60:
  grade = 'D'
else:
  grade = 'F'

print("Grade:", grade)'''

# 7.	Check if triangle is valid

'''sidea = int(input("Enter the value of side a : "))
sideb = int(input("Enter the value of side b : "))
sidec = int(input("Enter the value of side c : "))

if(sidea + sideb > sidec) and (sidec + sideb > sidea) and (sidea + sidec > sideb):
  print("Valid Triangle")
else:
  print("Invalid")'''

# 8.	Check if number is positive, negative or zero

'''a = int(input("Enter the value of a : "))

if(a==0):
  print("The numebr is zero")
elif(a>0):
  print("The number is positive")
else:
  print("The number is negative")'''

# 9.	Check if character is alphabet, digit or special character

'''a = input("Enter a character: ")

if a.isalpha():
    print("Alphabet")
elif a.isdigit():
    print("Digit")
else:
    print("Special Character")'''

# 10.	Calculate electricity bill with slabs

# 11.	Check if year is century year and leap year

'''year = int(input("Enter the year to check : "))

if(year % 400  == 0):
  print("It is a leap year and a Century")
elif(year % 4 == 0 and year % 100 != 0):
  print("It is a leap year and not a Century")
else:
  print("It is neither a leap year nor a Century")'''

# 12.	Find number of days in a month

'''year = int(input("Enter the year to check : "))
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
    print("Invalid Input")'''

# 13.	Check if point lies on x-axis, y-axis or origin

'''x = float(input("Enter the value of x-axis : "))
y = float(input("Enter the value of y-axis : "))

if x==0 and y==0:
  print("Point lies in the origin")
elif y==0:
  print("Point lies in the y-axis")
elif x==0:
  print("Point lies in the x-axis")
else:
  print("The point lies in the coordinate plane")'''

# 14.	Check if triangle is equilateral, isosceles or scalene

'''x = float(input("Enter the value of side x : "))
y = float(input("Enter the value of side y : "))
z = float(input("Enter the value of side z : "))

if (x + y > z) and (x + z > y) and (y + z > x):
  if x==y==z:
    print("Equilateral Triangle ")
  elif x==y or y==z or z==x:
    print("Isoceles Triangle")
  elif x!=y!=z:
    print("Scalene Triangle")

else:
  print("Invalid Triangle")'''

# 15.	Calculate roots of quadratic equation

# import math

'''a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

D = (b**2) - (4*a*c)

if D>0:
  root1 = (-b + math.sqrt(D)) / (2*a)
  root2 = (-b - math.sqrt(D)) / (2*a)
  print(f"The roots are real and distinct: {root1} and {root2}")

elif D==0:
  root1 = root2 = -b / (2*a)
  print(f"The roots are real and distinct: {root1} and {root2}")

elif D<0:
  real = -b / (2*a)
  imag = math.sqrt(abs(D)) / (2*a) #abs = absolute value i.e (-2)=2
  print(f"The roots are complex: {real}+{imag}i and {real}-{imag}i")'''