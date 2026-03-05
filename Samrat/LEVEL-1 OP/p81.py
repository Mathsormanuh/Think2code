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
prod=n
if len(primes)==0:
    prod=n-1
else:
    for i in primes:
        prod=prod*(1-1/i)
print(prod)