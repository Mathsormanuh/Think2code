n=int(input('Enter the number.\n'))
k=int(input('Enter the power.\n'))
s=1
for i in range (1,k+1):
    s=s*n
print('The required value is {}'.format(s))