#10.	Check if number is palindrome

num = int(input("Enter the number you want to check : "))

n = num
reverse = 0

while num > 0:
  last = num % 10
  reverse = (reverse*10)+last
  num = num // 10
  
if n == reverse:
  print("THe number is palidrome")
else:
  print("The number is not a palindrome")