array=[]
lnt=int(input('Enter the length of the array.\n'))
for i in range(lnt):
    array.append(int(input(f"Enter the {i+1}th element in the array.\n")))

max=0
for i in range(lnt):
    if array[i]>max:
        max=array[i]

print(f'The maximum value in the array is {max}')