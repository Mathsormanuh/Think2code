n=int(input())
pow2=[]
for i in range(1,n):
    if 3**i<=n:
        pow2.append(3**i)
if n in pow2:
    print('The number is a power of three.')
else:
    print('The number is not a power of three.')
    
