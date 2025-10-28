n = int(input("Enter rows: "))

# upper part
i = 1
while i <= n:
    print(" " * (n - i) + "*" * (2 * i - 1))
    i = i + 1

# lower part
i = n - 1
while i >= 1:
    print(" " * (n - i) + "*" * (2 * i - 1))
    i = i - 1