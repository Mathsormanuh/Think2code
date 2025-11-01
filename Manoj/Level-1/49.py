# 19.	Calculate sum of series 1 + 2 + 3 + ... + n

n = int(input("Enter the end range : "))
sum = 0
for i in range (1,n+1):
  sum = sum + i

print("The sum is : ",sum)