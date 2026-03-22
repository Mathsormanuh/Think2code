n=int(input())
factors=[]
for i in range(2,n):
    if n%i==0:
        factors.append(i)
primes=[]
for i in factors:
    isprime=True
    for j in range(2,i):
        if i%j==0:
            isprime=False
            break
    if isprime:
        primes.append(i)
if len(primes)==2:
    print('YES')
elif len(primes)==1:
    if primes[0]**2==n:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
