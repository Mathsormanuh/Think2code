n=int(input())
value=True
for i in range(2,int(n*(1/2))):
    if n%(i*i)==0:
        value=False
        break
if value:
    print('NO')
else:
    print('YES')
