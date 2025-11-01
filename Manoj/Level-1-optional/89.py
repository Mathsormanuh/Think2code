# 89.	Given n, print YES if n is a perfect number (sum of proper divisors equals n), else NO.

n = int(input("Enter the number you want to check : "))

sum = 0
for i in range(1,n,1):
  if (n % i )== 0:
    print(i)
    sum = sum+i
  
print(f"Sum of the Divisor is : {sum}")

if(sum == n):
  print(f"{n} is a perfect number")
else:
  print(f"{n} is not a perfect number")