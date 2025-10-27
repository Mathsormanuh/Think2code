n=input('Enter the number.\n')
m=len(n)
sum=0
for i in range (0,m):
    sum=sum+int(n[i])**int(m)
    print(sum)
if sum==int(n):
    print('The number is an Armstrong number.\n ')
else:
    print('The number is not an Armstrong number.\n')