a = int(input("Enter a: "))
b = int(input("Enter b: "))

total = 0
i = a
while i <= b:
    total = total + (i * i)
    i = i + 1

print("Sum of squares =", total)
