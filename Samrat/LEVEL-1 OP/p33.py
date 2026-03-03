n=int(input('Enter the number of rows required for half of the hourglass.\n'))
for i in range(n,0,-1):
    print(' '*(n-i)+'*'*(2*i-1))    
for i in range(1,n+1):
    print(' '*(n-i)+'*'*(2*i-1))
