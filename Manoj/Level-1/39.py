#9.	Reverse a number

num = int(input("Enter the number you want to reverse : "))

n = num
reverse = 0

while num > 0:
  last = num % 10
  reverse = (reverse*10)+last
  num = num // 10
  
print(f"The Reverse of the {n} is {reverse}")
