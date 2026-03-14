n=input('Enter the number separated by space.\n')
lst=[int(x) for x in n.split(' ')]
val=True
for i in range(len(lst)-1):
    if lst[i]<lst[i+1]:
        val=False

if val:
    print('It is strictly increasing.\n')
else:
    print('It is not strictly decreasing.\n')