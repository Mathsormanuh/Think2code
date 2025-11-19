a=int(input('Enter the value of a.\n'))
b=int(input('Enter the value of b (a<b).\n'))
prim=[]
for i in range(a,b+1):
    value=True
    for j in range(2,i):
        if i%j==0:
            value=False
            break
    if value:
        prim.append(i)
print(f'The set of primes are {prim}.')
