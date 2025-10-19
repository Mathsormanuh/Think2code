n=int(input('Enter the number.\n'))
a=0
for i in range(1,n):
    if n%i==0:
        a=a+i
    else:
        a=a
if n==a:
    print('The number is a perfect number.\n')
else:
    print('The number is not a perfect number.\n')
    
