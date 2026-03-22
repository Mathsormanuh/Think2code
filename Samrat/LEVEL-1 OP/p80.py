n=int(input())
factors=[]
for i in range(2,n):
    if n%i==0:
        factors.append(i)
primes=[]
print(factors)
for i in factors:
    isprime=True
    for j in range(2,i):
        if i%j==0:
            isprime=False
            break
    if isprime:
        primes.append(i)
print(primes)
squa=True
for i in primes:
    if n%(i**2)!=0:
        squa=False
        break

if squa:
    print('YES')
else:
    print('NO')