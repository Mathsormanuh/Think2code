n=int(input())
r=int(input())

def fac(n):
    prod=1
    for i in range(1,n+1):
        prod=prod*i
    return prod

print((fac(n))/(fac(n-r)*fac(r)))