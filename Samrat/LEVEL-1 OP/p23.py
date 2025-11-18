n=int(input(''))
print(' '*(n-1)+str(1)+' '*(n-1))
for i in range(2,n):
    print(' '*(n-i)+str(i)+' '*(2*i-3)+str(i)+' '*(n-i))
print(str(n)*(2*n-1))