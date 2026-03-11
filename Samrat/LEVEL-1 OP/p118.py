n=int(input())
if n%2!=0:
    print('The number is not divisible by two.\n')
else:
    for i in range(1,n):
        if n%2**(i+1)!=0:
            print(f'{2**(i)} is the required highest power.\n')
            break