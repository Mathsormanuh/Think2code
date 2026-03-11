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
for i in range(1,n+1):
    sum=sum+fac(i)

print(sum)