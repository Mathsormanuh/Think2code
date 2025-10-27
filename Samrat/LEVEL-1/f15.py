n=int(input('Enter the value of n.\n'))
#Right-Triangle
for i in range (1,n+1):
    print('x'*i)
m=int(input('Enter the value of m.\n'))
#Pyramid
for i in range (1,m+1):
    print(' '*(n-i)+'x'*(2*i-1))