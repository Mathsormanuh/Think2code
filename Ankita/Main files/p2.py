n = int(input("Enter a number: "))
sum = 0
i = 1
while i < n:
    if n % i == 0:
        sum = sum + i
    i = i + 1

if sum == n:
    print("Yes it is a perfect number")
else:
    print("No it is not a perfect number")