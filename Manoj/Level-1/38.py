# 8.	Find sum of digits of a number

n = int(input("Enter the number you want sum of : "))

sum = 0
num = n

if n<10:
  sum = n

else:
  while n > 0:
    last = n % 10
    sum = sum + last
    n = n // 10
  
print(f"The Sum of digit of {num} is {sum}")
