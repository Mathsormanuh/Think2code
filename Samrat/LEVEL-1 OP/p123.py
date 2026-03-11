n=int(input())
stir=''
while n!=1:
    stir=str(n%2)+stir
    n=n//2

print(str(1)+stir)