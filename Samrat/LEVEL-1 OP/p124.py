n=int(input())
stir=''
while n!=1:
    stir=str(n%2)+stir
    n=n//2

bi=str(1)+stir
one=0
for item in bi:
    if item=='0':
        one=one+1

print(one)