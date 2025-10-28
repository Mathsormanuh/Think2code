a = int(input("Enter a: "))
b = int(input("Enter b: "))

total = 0
i = a

while i <= b:
    if i % 3 != 0:          
        total = total + i   
    i = i + 1               

print("Sum of numbers not multiple of 3 =", total)