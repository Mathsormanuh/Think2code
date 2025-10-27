n=int(input('Enter the value of n.\n'))
value=True
for i in range (2,n):
    if n%i==0:
        value=False
        break
print(value)
if value==True:
    print('The number is a prime number.\n')
else:
    print('The number is not a prime number.\n')