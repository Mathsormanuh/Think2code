def fac(n):
    if n==0:
        prod=1
    else:
        prod=1
        for i in range(1,n+1):
            prod=prod*i
    return prod
n=int(input())
for i in range(0,n+1):
    sum=0
    for j in range(0,i+1):
        sum+=int(fac(i)/(fac(i-j)*fac(j)))
    print(sum)