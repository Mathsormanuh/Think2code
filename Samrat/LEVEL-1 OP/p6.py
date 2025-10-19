a=int(input('Enter the first value.\n'))
b=int(input('Enter the second value.(This must be larger than the previous one.)\n'))
s=0
for i in range (a,b+1):
    if i%3!=0:
        s+=i
print('The sum of the numbers not divisible in [{},{}] is {}'.format(a,b,s))