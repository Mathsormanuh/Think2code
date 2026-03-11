def fac(n):
    prod=1
    for i in range(1,n+1):
        prod=prod*i
    return prod

n=int(input())
a=1
b=1
print(1)
print(1)
for i in range(3,n+1):
    x=int((fac(2*i))/(fac(i+1)*fac(i)))
    print(x)
