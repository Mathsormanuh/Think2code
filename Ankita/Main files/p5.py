a = int(input("Enter a: "))
b = int(input("Enter b: "))
k = int(input("Enter k: "))

count = 0
i = a
while i <= b:
    if i % k == 0:
        count = count + 1
    i = i + 1
print("Count of multiples of", k, "=", count)