# 14.	Swap numbers without temporary variable

a = int(input("Enter the number of a : "))
b = int(input("Enter the number of b : "))
print(f"Before Swapping : a = {a}, b = {b}")

a, b = b, a  

print(f"After Swapping : a = {a}, b = {b}")