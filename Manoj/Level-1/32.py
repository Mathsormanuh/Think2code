# 2.	Print even numbers from 1 to n

n = int(input("Enter the end number : "))

for i in range(n):
  if i % 2 == 0:
    print("Even count is : ",i)