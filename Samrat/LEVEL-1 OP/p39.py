n=int(input('Entere the number of rows.\n'))
if n%2==0:
    for i in range(1,int(n/2)):
        print(' '*(n-i)+'*'*(2*i-1))
    for i in range(int(n/2)+1,0,-1):
        print(' '*(n-i)+'*'*(2*i-1))
else:
    for i in range(1,int((n+1)/2)):
        print(' '*(n-i)+'*'*(2*i-1))
    for i in range(int((n+1)/2),0,-1):
        print(' '*(n-i)+'*'*(2*i-1))