n=int(input('Enter the number of rows.\n'))
print('*'*n)
for i in range(n-2):
    print('*',end='')
    for k in range(i):
        print(' ',end='')
    print('*',end='')
    for k in range(n-3-i):
        print(' ',end='')
    print('*',end='')
    print()
print('*'*n)