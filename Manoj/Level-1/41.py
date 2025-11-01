#11.	Find Armstrong number

num = int(input("Enter the number you want to check : "))
count = len(str(num))
n = num
sum = 0

while n > 0:
  last = n % 10
  sum = sum + (last ** (count))
  n = n // 10
print(sum)
  
if sum == num:
  print("The number is armstrong")
else:
  print("The number is not armstrong")


