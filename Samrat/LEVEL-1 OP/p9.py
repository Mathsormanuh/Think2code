a=int(input('Enter the first value.\n'))
b=int(input('Enter the second value.(This must be larger than the previous one.)\n'))
ast=str(a)
bst=str(b)
s=0
for i in range (a,b):
    if int(len(str(i)))%2==0:
        s+=1
    else:
        s=s
print('The total numbers with even count are {}'.format(s))