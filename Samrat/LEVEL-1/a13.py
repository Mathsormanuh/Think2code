n=int(input('Enter the length of the first array.\n'))
arr=[]
nm=[]
for i in range(n):
    arr.append(int(input(f'Enter the {i+1}th value.\n')))
unique=[]
for i in arr:
    if i not in unique:
        unique.append(i)
lns=len(unique)
print(lns)
print(unique)
for i in range(lns):
    iter=0
    for j in range(n):
        if unique[i]==arr[j]:
            iter+=1
        else:
            iter=iter
    print(f'The frequency of {unique[i]} is {iter}.')
    
