n=int(input('Enter the number.\n'))
a=0
for i in range(1,n):
    if n%i==0:
        a=a+i
    else:
        a=a
if n==a:
    print('The number is a perfect number.\n')
elif a>n:
    print('The number is abundant.')
else:
    print('The number is deficient.\n')