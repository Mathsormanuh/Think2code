n=int(input('Enter the length of the first array.\n'))
arr=[]
for i in range(n):
    arr.append(int(input(f'Enter the {i+1}th value.\n')))
m=int(input('Enter the length of the second array.\n'))
arr2=[]
for j in range(m):
    arr2.append(int(input(f'Enter the {j+1}th value.\n')))
print(f'The merged array is {arr+arr2}')