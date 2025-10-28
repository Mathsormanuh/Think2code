a = int(input("Enter a: "))
b = int(input("Enter b: "))

i = a
while i <= b:
    if i > 1:
        j = 2
        while j < i:
            if i % j == 0:
                break
            j = j + 1
        else:
            print(i)
    i = i + 1
