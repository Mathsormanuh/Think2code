first=int(input('Enter the first number.\n'))
second=int(input('Enter the second number.\n'))
HCF=0
for i in range (1,first*second):
    if first%i==0 and second%i==0:
        HCF=i
print('The HFC of the two numbers are {}'.format(HCF))