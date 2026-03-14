n=input('Enter the number separated by space.\n')
lst=[int(x) for x in n.split(' ')]
br_ind=[]
for i in range(len(lst)-1):
    if lst[i]>lst[i+1]:
        br_ind.append(i+1)
br_ind.append(len(lst)-1)
diff=0
u=0
l=0
val=[]
for i in range(len(br_ind)-1):
    if diff<br_ind[i+1]-br_ind[i]:
        diff=br_ind[i+1]-br_ind[i]
        u=br_ind[i+1]
        l=br_ind[i]

res=[]
for x in range(l,u):
    res.append(lst[x])

print(res)


