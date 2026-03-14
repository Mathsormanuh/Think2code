n=input('Enter the number separated by space.\n')
lst=[int(x) for x in n.split(' ')]
k=int(input('Enter the number positions the list is to be shifted left.\n'))
new_lst=[]
for i in range(k,0,-1):
    new_lst.append(lst[-i])
for i in range(0,len(lst)-k):
    new_lst.append(lst[i])

print(new_lst)
