a = int(input("Enter a: "))
b = int(input("Enter b: "))

max_sum = -1
best = a

i = a
while i <= b:
    s = 0
    for ch in str(i):
        s = s + int(ch)
    if s > max_sum:
        max_sum = s
        best = i
    elif s == max_sum and i < best:
        best = i
    i = i + 1

print("Number with max digit sum =", best)
