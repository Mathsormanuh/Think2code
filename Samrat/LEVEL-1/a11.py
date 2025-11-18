n=int(input('Enter the length of the array.\n'))
arr1=[]
for i in range(n):
    arr1.append(int(input(f'Enter the {i+1}th value.\n')))
unique=[]
for i in arr1:
    if i not in unique:
        unique.append(i)
print(f'The array with no repeated elements is {unique}')