# 13.	Find LCM of two numbers

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

max_number = max(a,b)
multiply =  a * b

for i in range(max_number,multiply+1):
  if i % a == 0 and i % b == 0:
    lcm = i
    break

print(f"The lcm of the number {a} and {b} is {lcm}")