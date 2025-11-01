# 93.	Given a and b, print the sum of all numbers in [a, b] that are not multiples of 3.

a = int(input("Enter the starting value : "))
b = int(input("Enter the ending value : "))

sum = 0
for i in range(a,b+1,1):
  if i % 3 == 0:
    print(i)
    sum = sum + i

print("Sum is : ",sum)