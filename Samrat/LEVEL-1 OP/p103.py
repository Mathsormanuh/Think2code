def fac(n):
    prod=1
    for i in range(1,n+1):
        prod=prod*i
    return prod

def comb(n,r):
    return int((fac(n))/(fac(n-r)*fac(r)))

def stir(n,k):
    sum=0
    for j in range(0,k+1):
        sum=sum+((-1)**(k-j))*comb(k,j)*(j**n)
    return int((1/fac(k))*sum)

m=int(input())
sum=0
for i in range(1,m+1):
    sum=sum+stir(m,i)

print(int(sum))