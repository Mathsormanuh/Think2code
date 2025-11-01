# 88. Given n, print YES if n is a perfect square, else NO.

n = int(input("Enter the number you want to check : "))

a = n ** (1/2)
round_a = round(a)

if(a == round_a):
  print(f"{n} is a perfect square")
else:
  print(f"{n} is not a perfect square")