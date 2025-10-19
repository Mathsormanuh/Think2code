'''a=int(input('Enter the first value.\n'))
b=int(input('Enter the second value.(This must be larger than the previous one.)\n'))
m=int(input('Enter the divisor.\n'))
s=0

for i in range (a,b+1):
    if i%m==0:
        s=i
if s==0:
    print('The lasgest multiple is -1.')
else:
    print('The largest multiple of {} is {}'.format(m,s))'''


a = int(input('Enter the first value.\n'))
b = int(input('Enter the second value. (This must be larger than the previous one.)\n'))
m = int(input('Enter the divisor.\n'))

# Find the largest multiple of m less than or equal to b
largest_multiple = (b // m) * m

# Check if it's within the range
if largest_multiple < a:
    print('The largest multiple is -1.')
else:
    print(f'The largest multiple of {m} is {largest_multiple}')
