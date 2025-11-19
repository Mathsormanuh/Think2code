# 95.	Given a and b, print the largest number in [a, b] that is a multiple of m (or print -1 if none).

a = int(input("Enter the starting value : "))
b = int(input("Enter the ending value : "))

m = int(input("Enter the number you want multiples of : "))

largest_element = -1

for i in range(a,b+1):
  if i % m == 0:
    largest_element = i

print(f"The largest numebr in [{a},{b}] is {largest_element}")