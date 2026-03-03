n=int(input('Enter the number of rows.\n'))
value=1
for i in range(1,n+1):
    print(' '*(n-i+1),end='')
    for j in range(0,2*i-1):
        print(value,end='')
        value+=1
    print()