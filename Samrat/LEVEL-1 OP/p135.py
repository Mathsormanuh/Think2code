n=int(input('Enter the value of n.\n'))
r=int(input('Enter the value of r.\n'))

def fac(n:int)->int:
    prod=1
    for i in range(1,n+1):
        prod=prod*i
    return prod

print(int((fac(n))/(fac(n-r)*fac(r))))