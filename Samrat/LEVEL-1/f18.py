n=int(input('Enter the value of n.\n'))
print('The prime factors are\n')
for i in range (1,n+1):
    if n%i==0:
        print(i)
