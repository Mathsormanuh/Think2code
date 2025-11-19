n=int(input('Enter the length of the array.\n'))
arr1=[]
for i in range(n):
    arr1.append(int(input(f'Enter the {i+1}th value.\n')))

odd=0
even=0
for i in range(n):
    if int(arr1[i])%2==0:
        even=even+1
    else:
        odd=odd+1
print(f'The number of even and odd elements is {even} and {odd}')