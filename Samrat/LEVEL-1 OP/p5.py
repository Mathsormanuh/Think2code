a=int(input('Enter the first value.\n'))
b=int(input('Enter the second value.(This must be larger than the previous one.)\n'))
k=int(input('Enter the value for which the multiple is to be calculated.\n'))
s=0
for i in range (a,b+1):
    if i%k==0:
        s+=1
    else:
        s=s

print('The count of multiples in [{},{}] is {}'.format(a,b,s))