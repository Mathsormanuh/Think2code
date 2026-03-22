n=int(input())
factors=[]
for i in range(2,n):
    if n%i==0:
        factors.append(i)
primes=[]
for i in factors:
    is_prime=True
    for j in range(2,i):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        primes.append(i)
sum=0
for i in primes:
    sum+=i
print(sum)