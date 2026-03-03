n=int(input('Enter the number of rows.\n'))
for i in range(n+1):
    print(' '*(n-i)+'*'*(2*i-1))
for i in range(n,0,-1):
    print(' '*(n-i)+'*'*(2*i-1))