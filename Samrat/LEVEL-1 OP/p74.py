n=int(input())
factors=[]
prime=[]
for i in range(1,n):
    if n%i==0:
        factors.append(i)
isprime=True
for item in factors:
    if item==2 or item==3:
        prime.append(item)
    if item>3:
        for j in range(2,item):
            if item%j==0:
                isprime=False
                break
        if isprime:
            prime.append(item)
    isprime=True
print(prime[0])
