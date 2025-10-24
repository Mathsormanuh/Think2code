# 4.	Calculate sum of first n natural numbers

n = int(input("Enter the end number : "))

Sum = 0
for i in range(1,n+1):
  Sum = Sum + i

print("Sum is : ",Sum )