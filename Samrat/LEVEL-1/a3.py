ar=[]
sum=0
num=int(input('Enter the length of the array.\n'))
for i in range(num):
    ar.append(int(input(f'Enter the {i+1}th value of the array.\n')))
    sum=ar[i]+sum
print(f'The array is {ar} and the sum of its elements are {sum}.')

