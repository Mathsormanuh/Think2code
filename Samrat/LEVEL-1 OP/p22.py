n=int(input('Enter the height of the pyramid.\n'))
for i in range(1,n+1):
    print(' '*(n-i)+str(i)*(2*i-1)+' '*(n-i))