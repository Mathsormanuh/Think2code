a=int(input('Enter the first value.\n'))
b=int(input('Enter the second value.(This must be larger than the previous one.)\n'))
s=0
for i in range (a,b+1):
    if i%2==0:
        s+=1
    else:
        s=s

print('The number of even numbers in [{},{}] is {}'.format(a,b,s))