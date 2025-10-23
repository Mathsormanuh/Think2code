# Basic Syntax & Variables
# 1.	Print "Hello, World!"

"""print("Hello, World!")"""

# 2.	Declare variables of different data types

""" integer = 10
string = "Hello World"
float = 9.999
boolean = True
list = [1, 2, 3, "apple", "banana"]

print(type(integer))
print(type(string))
print(type(float))
print(type(boolean))
print(type(list)) """

# 3.	Swap values of two variables

"""a = int(input("Enter the number of a : "))
b = int(input("Enter the number of b : "))
print(f"Before Swapping : a = {a}, b = {b}")

temp = a
a = b
b = temp
print(f"After Swapping : a = {a}, b = {b}")"""

# 4.	Calculate sum of two numbers

"""a = int(input("Enter the number of a : "))
b = int(input("Enter the number of b : "))

sum = a + b
print("Sum is : ",sum)"""

# 5.	Calculate area of a rectangle

'''length = int(input("Enter the length of the rectangle : "))
width = int(input("Enter the width of the rectangle : "))

Area = length * width

print("Area is :",Area)'''

# 6.	Convert Celsius to Fahrenheit

'''celsius = float(input("Enter the temperature in celsius : "))

fahrenheit = (celsius * 9/5) + 32 

print("Temperature in fahrenheit : ",fahrenheit)'''

# 7.	Calculate simple interest

'''principal = float(input("Enter the principal amount : "))
rate = float(input("Enter the rate of interest : "))
time = float(input("Enter the time period : "))

simple_interest = (principal * rate * time) / 100

print("Simple interest is : ",simple_interest)'''

# 8.	Check if number is positive or negative

'''a = int(input("Enter the number of a : "))

if(a==0):
  print("The number is neither positive nor negative")
elif(a>0):
  print("The number is positve")
else :
  print("The number is negative")'''

# 9.	Find remainder of division

'''dividend = int(input("Enter the dividend : "))
divisor = int(input("Enter the divisor : "))

remainder = dividend%divisor

print(f"The remainder of {dividend} divided by {divisor} is: {remainder}")'''

# 10.	Convert minutes to hours

'''minutes = int(input("Enter the minutes : "))

hour = minutes / 60

print(f"{minutes} in Hour is {hour}")'''

# 11.	Calculate BMI (Body Mass Index)

'''weight = float(input("Enter the weight of the person (kg) : "))
height = float(input("Enter the height of the person (m) : "))

BMI = weight / ((height)**2)

print("Person BMI is : ", BMI)'''

# 12.	Convert kilometers to miles

'''kilo = float(input("Enter the distance in kilometer : "))

miles = kilo * 0.62

print(f"{kilo} km in miles is : {miles}")'''

# 13.	Calculate profit or loss percentage

'''cost = float(input("Enter the cost price : "))
sell = float(input("Enter the selling price : "))

if(sell>cost):
  profit = sell - cost
  profit_percent = (profit/cost)* 100
  print("Profit is : ",profit_percent)
elif(cost>sell):
  loss = cost - sell
  loss_percent = (loss/cost)*100
  print("Loss is : ",loss_percent)

else:
  print("NO profit NO loss") '''

# 14.	Swap numbers without temporary variable

'''a = int(input("Enter the number of a : "))
b = int(input("Enter the number of b : "))
print(f"Before Swapping : a = {a}, b = {b}")

a, b = b, a  

print(f"After Swapping : a = {a}, b = {b}")'''

# 15.	Calculate compound interest

'''principal = float(input("Enter the principal amount : "))
rate = float(input("Enter the rate of interest : "))
time = float(input("Enter the time period : "))
frequency = float (input("Interest compound in a year : "))

future_value = principal * ((1 + rate / frequency)**(frequency * time))

compound_interest = future_value - principal

print("Compound Interest is : ",compound_interest)'''