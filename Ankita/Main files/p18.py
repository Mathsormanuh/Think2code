n = int(input("Enter rows: "))
i = 1
while i <= n:
    print(" " * (n - i) + "*" * (2 * i - 1))
    i = i + 1