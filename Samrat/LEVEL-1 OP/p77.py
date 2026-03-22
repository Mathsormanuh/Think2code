n=int(input())
sum=0
isprime=True
for i in range(2,n):
    if n%i==0:
        isprime=False
if isprime:
    sum=n
else:
    for i in range(2,n):
        if n>2:
            if n%i==0:
                sum+=i
                n=n/i
        else:
            break
print(sum)