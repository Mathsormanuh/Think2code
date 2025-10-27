a=int(input('Enter the first number.\n'))
b=int(input('Enter the second number.\n'))
c=int(input('Enter the third number.\n'))

if a<b:
    if b<c:
        print('The largest number is {}.'.format(c))
    else:
        print('The largest number is {}.'.format(b))
elif a>b and a>c:
    print('The largest number is {}.'.format(a))
