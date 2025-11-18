st=input('Enter the string.\n')
n=len(st)
uniq=[]
for i in range(n):
    if st[i] not in uniq:
        uniq.append(st[i])
m=len(uniq)
max=0
ap=st[0]
for i in range(m):
    iter=0
    for j in range(n):
        if uniq[i]==st[j]:
            iter=iter+1
        else:
            iter=iter
    if max>=iter:
        max=max
    else:
        max=iter
        ap=uniq[i]

print(f'The maximum frequency is {max} for the letter {ap}')