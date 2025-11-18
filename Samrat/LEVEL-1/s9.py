st=input('Enter the string.\n')
uniq=[]
n=len(st)
for i in range(n):
    if st[i] not in uniq:
        uniq.append(st[i])
m=len(uniq)
for i in range(m):
    iter=0
    for j in range(n):
        if uniq[i]==st[j]:
            iter+=1
        else:
            iter=iter
    print(f'The frequency of {uniq[i]} is {iter}')
    