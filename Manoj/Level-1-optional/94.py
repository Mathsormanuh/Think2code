# 94.	Given a and b, print the sum of squares of all numbers in [a, b].

a = int(input("Enter the starting value : "))
b = int(input("Enter the ending value : "))

sum = 0
for i in range(a,b+1,1):
  square = i*i
  sum = sum + square

print(f"The sum of squares of all number between [{a},{b}] is {sum}")