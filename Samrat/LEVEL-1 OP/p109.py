def fac(n):
    if n==0:
        prod=1
    else:
        prod=1
        for i in range(1,n+1):
            prod=prod*i
    return prod
ls=[]
n=int(input())
for i in range(0,n*2):
    for j in range(0,i+1):
        x=int(fac(i)/(fac(i-j)*fac(j)))
        ls.append(x)

if n in ls:
    print('YES')
else:
    print('NO')
