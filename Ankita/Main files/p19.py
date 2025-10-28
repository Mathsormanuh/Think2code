n = int(input("Enter rows: "))
i = n
while i >= 1:
    print(" " * (n - i) + "*" * (2 * i - 1))
    i = i - 1