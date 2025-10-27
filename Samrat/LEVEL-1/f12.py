first=int(input('Enter the first number.\n'))
second=int(input('Enter the second number.\n'))
LCM=0
for i in range (1,first*second):
    if i%first==0 and i%second==0:
        LCM=i
        break
print('The LCM of the two numbers are {}'.format(LCM))