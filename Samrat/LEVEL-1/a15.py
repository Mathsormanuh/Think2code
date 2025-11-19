n1=int(input('Enter the length of the first array.\n'))
n2=int(input('Enter the length of the second array.\n'))
ar1=[]
ar2=[]
common=[]
for i in range(n1):
    ar1.append(int(input(f'Enter the {i+1}th element.\n')))
for i in range(n2):
    ar2.append(int(input(f'Enter the {i+1}th element.\n')))
common=[]
union=ar1+ar2
for i in union:
    if i in ar1 and i in ar2 and i not in common:
        common.append(i)
print(f'The common elements are {common}')