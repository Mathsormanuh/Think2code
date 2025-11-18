array=[]
lnt=int(input('Enter the length of the array.\n'))
for i in range(lnt):
    array.append(int(input(f"Enter the {i+1}th element in the array.\n")))

min=array[0]
print(min)
for i in range(lnt):
    if array[i]>=min:
        min=min
    else:
        min=array[i]

print(f'The minimum value in the array is {min}')