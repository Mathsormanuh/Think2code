a = int(input("Enter a: "))
b = int(input("Enter b: "))

lcm = a
i = a + 1
while i <= b:
    j = 1
    while (lcm * j) % i != 0:
        j = j + 1
    lcm = lcm * j
    i = i + 1

print("LCM =", lcm)
