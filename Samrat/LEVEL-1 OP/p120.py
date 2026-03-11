n=int(input())
pow2=[]
for i in range(1,n):
    if 2**i<=n:
        pow2.append(2**i)
if n in pow2:
    print('The number is a power of two.')
else:
    print('The number is not a power of two.')
    
