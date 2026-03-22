n=int(input('Enter the number.\n'))
p=int(input('Enter the prime.\n'))
if n%p!=0:
    print(f'The number is not divisible by {p}.\n')
else:
    for i in range(1,n):
        if n%p**(i+1)!=0:
            print(f'{p**(i)} is the required highest power.\n')
            break