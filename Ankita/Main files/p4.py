a = int(input("Enter a: "))
b = int(input("Enter b: "))

count = 0
i = a
while i <= b:
    if i % 2 == 0:
        count = count + 1
    i = i + 1

print("Count of even numbers =", count)
