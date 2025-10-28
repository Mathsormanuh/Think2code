n = int(input("Enter a number: "))

if n<2:
    print("No it is not a prime")
else:
    i = 2
    while i < n:
        if n % i == 0:
            print("No it is not a prime ")
            break
        i = i + 1
    else:
        print("Yes it is a prime")
