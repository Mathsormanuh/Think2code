ar=[]
num=int(input('Enter the length of the array.\n'))
for i in range(num):
    ar.append(int(input(f'Enter the {i+1}th element.\n')))
k=int(input('For the n-th value of the array, enter n.\n'))
print(f'The array is {ar} and the {k}th value is {ar[k]}')