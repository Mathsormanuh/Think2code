n=int(input())
prim=[]
for i in range(2,n):
    while n%i==0:
        prim.append(i)
        n=n//i
prod=1
uniq=[]
for items in prim:
    if items not in uniq:
        uniq.append(items)
for item in uniq:
    if item==2:
        count=0
        for i in prim:
            if i==2:
                count+=1
        prod=prod*(2**(count-2))
    else:
        count=0
        for i in prim:
            if i==item:
                count+=1
        prod=prod*(item-1)*(item**(count-1))
print(prod)