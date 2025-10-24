# 5.	Calculate factorial of a number

n = int(input("Enter the number : "))

fact = 1
for i in range(n,0,-1):
  fact = fact * i

print("Factorial is : ",fact)