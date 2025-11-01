# 20.	Find factorial using while loop

n =  int (input("Enter the number : "))

fact = 1
i = 1
while i <= n:
  fact = fact * i
  i = i + 1

print("The factorial of the number is : ",fact)