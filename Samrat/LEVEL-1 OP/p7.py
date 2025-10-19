a=int(input('Enter the first value.\n'))
b=int(input('Enter the second value.(This must be larger than the previous one.)\n'))
s=0
for i in range (a,b+1):
    s+=(i*i)

print('The sum of squares in [{},{}] is {}'.format(a,b,s))