# 3.	Swap values of two variables

a = int(input("Enter the number of a : "))
b = int(input("Enter the number of b : "))
print(f"Before Swapping : a = {a}, b = {b}")

temp = a
a = b
b = temp
print(f"After Swapping : a = {a}, b = {b}")