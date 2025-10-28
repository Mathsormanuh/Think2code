a = int(input("Enter a: "))
b = int(input("Enter b: "))
m = int(input("Enter m: "))

largest = -1
i = b
while i >= a:
    if i % m == 0:
        largest = i
        break
    i = i - 1

print(largest)
