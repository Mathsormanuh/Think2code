def fac(n):
    if n==0:
        prod=1
    else:
        prod=1
        for i in range(1,n+1):
            prod=prod*i
    return prod

n=int(input())
print(int((fac(2*n))/(fac(n)**2)))