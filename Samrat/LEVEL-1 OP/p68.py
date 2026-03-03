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

for i in range(int(len(lst)-1)):
    if lst[i]+2==lst[i+1]:
        print((lst[i],lst[i+1]))