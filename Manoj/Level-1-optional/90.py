# 90.	Given n, print YES if n is abundant, deficient, or perfect (exactly one word).

n = int(input("Enter the number you want to check : "))

sum = 0
for i in range(1,n,1):
  if (n % i )== 0:
    print(i)
    sum = sum+i

print(f"Sum of the Divisor is : {sum}")

if n > sum:
  print("Dificient")
elif n < sum:
  print("Abundant")
elif n==sum:
  print("Perfect")