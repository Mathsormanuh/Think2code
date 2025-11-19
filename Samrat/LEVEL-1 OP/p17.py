n=int(input('Enter the number of rows.\n'))
for i in range(1,n+1):
    print(' '*(n-i))
    for j in range(1,i+1):
        print(j,end=' ')