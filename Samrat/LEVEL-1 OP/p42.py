n=int(input('Enter the number of rows.\n'))
if n%2!=0:
    print('10'*int(n/2))
    for i in range(0,n-2):
        print('1'+' '*(n-3)+'0')
    print('01'*int(n/2))
else:
    print('10'*int(n/2))
    for i in range(0,n-2):
        print('1'+' '*(n-2)+'0')
    print('01'*int(n/2))