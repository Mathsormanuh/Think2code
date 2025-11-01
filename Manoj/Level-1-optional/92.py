# Given a and b, print the count of multiples of k in [a, b] (user gives k).

a = int(input("Enter the starting value : "))
b = int(input("Enter the ending value : "))

k = int(input("Enter the number you want multiples of : "))

count = 0
for i in range(a,b+1,1):
  if i % k == 0:
    print(i)
    count = count + 1

print("Count is : ",count)