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
    if isprime:
        primes.append(i)
value=0
vax=True
for item in primes:
        if n%(item**2)==0:
            vax=False
            break
if vax:
    if len(primes)>1:
        value=(-1)**(len(primes))
    elif n==1:
        value==1
    else:
        value=-1
else:
    value=0

print(value)