def bin(n):
    stir=''
    while n!=1:
        stir=str(n%2)+stir
        n=n//2
    return str(1)+stir

def coun(n):
    c1=0
    for item in n:
        if item=='1':
            c1+=1
    return c1
n=int(input())
nb=bin(n)
n1=coun(nb)
for k in range(n+1,2*n):
    if coun(bin(k))==n1:
        large_n=k
        break

print(f'The required number is {large_n}')