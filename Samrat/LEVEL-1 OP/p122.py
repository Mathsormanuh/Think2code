n=int(input('Enter the value of n.\n'))
k=int(input('Enter the value of k.\n'))
pow2=[]
for i in range(1,n):
    if k**i<=n:
        pow2.append(k**i)
if n in pow2:
    print(f'The number is a power of {k}.')
else:
    print(f'The number is not a power of {k}.')
    
