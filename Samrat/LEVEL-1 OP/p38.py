n=int(input('Enter the height of the triangle.\n'))
for i in range(n):
    if i==1 or i==0:
        print('*'*i)
    else:
        print('*'+' '*(i-2)+'*')
print('*'*(n))