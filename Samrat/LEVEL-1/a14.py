n=int(input('Enter the length of the first array.\n'))
arr=[]
for i in range(n):
    arr.append(int(input(f'Enter the {i+1}th value.\n')))
arr.sort( )
print(f'The sorted array is {arr}')