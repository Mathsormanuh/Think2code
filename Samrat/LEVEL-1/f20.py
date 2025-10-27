n=int(input('Enter the number.\n'))
prod=1
for i in range (1,n+1):
    prod=prod*i
print('The factorial of {} is {}'.format(n,prod))