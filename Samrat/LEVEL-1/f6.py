n=int(input('Enter the number of terms (Number of terms must be greater than 2).\n'))
a0=1
a1=1
print('The fibonacci series is:\n')
print(a0)
print(a1)
for i in range (2,n+1):
    a2=a1+a0
    print(a2)
    a0=a1
    a1=a2
