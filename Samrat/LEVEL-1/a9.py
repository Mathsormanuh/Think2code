n=int(input('Enter the length of the array.\n'))
arr1=[]
for i in range(n):
    arr1.append(int(input(f'Enter the {i+1}th value.\n')))

ps=0
ng=0
for i in range(n):
    if int(arr1[i])>0:
        ps=ps+1
    elif int(arr1[i])<0:
        ng=ng+1
    else: 
        ps=ps
        ng=ng
print(f'The number of positive and negative elements is {ps} and {ng}')