n=int(input())
isprime=True
lst=[]

for i in range(n,2*n+1):
    for j in range(2,i):
        if i%j==0:
            isprime=False
    if isprime:
        lst.append(i)
    isprime=True
for item in lst:
    print(item,end=' ')