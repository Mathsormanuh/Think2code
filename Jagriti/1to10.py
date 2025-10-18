#Basic Syntax & Variables (15 problems)
#p 1.Print "Hello, World!"
print("hello world")

#p 2.Declare variables of different data types
num = 10
price = 99.99
name = "Jiya"
is_student = True
fruits =["banana", "mango", "grapes"]
coordinates = (1,2)
person ={"name": "Jiya", "age": 20}
unique_numbers = {1,2,3,4,5}

#p 3.Swap values of two variables
a= 1
b= 2
a,b = b,a
print(a,b)

#p 4.Calculate sum of two numbers
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
print("sum:",a + b)

#p 5.	Calculate area of a rectangle
length = float(input("length:"))
width = float(input("width:"))
area = length*width
print("area of the rectangle is:",area)

#p 6.Convert Celsius to Fahrenheit
c = float(input("celsius:"))
f = (c*9/5)+32
print("fahrenheit:",f)

# 7.Calculate simple interest
p = float(input("principal:"))
r = float(input("rate(annual %):"))
t = float(input("time(years):"))
simple_interest= (p*r*t)/100
print("simple interest:",simple_interest)

#p 8.Check if number is positive or negative
n = float(input("Number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

# 9.Find remainder of division
a = int(input("Dividend: "))
b = int(input("Divisor: "))
remainder = a % b
print("Remainder:", remainder)

#p 10.Convert minutes to hours
minutes = int(input("Minutes: "))
hours = minutes // 60
mins = minutes % 60
print(f"{hours} hour(s) and {mins} minute(s)")

