def fac(n):
    prod=1
    if n==0 or n==1:
        prod=1
    else:
        for i in range(1,n+1):
            prod=prod*i
    return prod

n=int(input())
sum=0
for i in range(0,n+1):
    sum=sum+((-1)**i)*(1/(fac(i)))

print(int(fac(n)*sum))

