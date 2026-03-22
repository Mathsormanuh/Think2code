n=input('Enter the number separated by space.\n')
lst=[int(x) for x in n.split(' ')]
val=True
for i in range(len(lst)-1):
    if lst[i+1]>lst[i]:
        val=False
if val:
    print('It is strictly decreasing.\n')
else:
    print('It is not strictly decreasing.\n')