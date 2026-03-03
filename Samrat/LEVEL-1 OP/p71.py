import math
n=int(input('Enter the value of n.\n'))
k=2
isprime=True
lst=[]
for i in range(n**n):
    for j in range(2,k):
        if k%j==0:
            isprime=False
    if isprime:
        lst.append(k)
    isprime=True
    k=k+1
    if len(lst)==n:
        break
if math.log2(n-1).is_integer():
    print('It is a Mersenne number.\n')
else:
    print('It is not a Mersenne number.\n')
