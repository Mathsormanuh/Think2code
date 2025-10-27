n=int(input('Enter the value of n.\n'))
sum=0
for i in range (1,n+1):
    sum=sum+i
print('The sum of the first {} natural number is {}.'.format(n,sum))