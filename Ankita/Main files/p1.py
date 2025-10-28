n = int(input("Enter a number: "))

# Simple logic
i = 1
while i * i <= n:
    if i * i == n:
        print(n, "is a perfect square")
        break
    i = i + 1
else:
    print(n, "is not a perfect square")