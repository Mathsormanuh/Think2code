n=int(input('Enter the number of rows.\n'))
for i in range(1,n+1):
    if i%2==0:
        print('*'*n)
    else:
        print(' '*n)