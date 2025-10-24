# 3.	Print multiplication table

n = int(input("Enter the a number : "))
r = int(input("Enter range: "))

for i in range(1 , r+1):
  print(f"{n} X {i} = {n * i}")