n=int(input('Enter the length of the array.\n'))
arr1=[]
for i in range(n):
    arr1.append(int(input(f'Enter the {i+1}th value.\n')))
max=arr1[0]
for i in range(n):
    if arr1[i]<=max:
        max=max
    else:
        max=arr1[i]
print(max)
arr1.remove(max)
print(arr1)
max2=arr1[0]
for i in range(n-1):
    if arr1[i]<=max2:
        max2=max2  
    else:
        max2=arr1[i]
print(f'The second largest element is {max2}.')