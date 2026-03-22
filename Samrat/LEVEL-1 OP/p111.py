def fac(n):
    if n==0 or n==1:
        prod=1
    else:
        prod=1
        for i in range(1,n+1):
            prod=prod*i
    return prod

def com(n,r):
    return int((fac(n))/(fac(n-r)*fac(r)))

n=int(input())
k=int(input())
sum=0
for i in range(0,k+1):
    sum=sum+(-1)**i*com(k,i)*(k-i)**n

print(int(sum/(fac(k))))