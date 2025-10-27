n=input('Enter the value of n.\n')
length=len(n)
sum=0
for i in range (0,length):
    sum=sum+int(n[i])
print('The sum of the numbers of {} is {}.\n'.format(n,sum))