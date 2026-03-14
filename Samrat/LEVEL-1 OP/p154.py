n=input('Enter the number separated by space.\n')
lst=[int(x) for x in n.split(' ')]
sort_lst=sorted(lst)
val=True
for i in range(len(lst)):
    if lst[i]!=sort_lst[i]:
        val=False
if val:
    print('It is sorted.\n')
else:
    print('It is not sorted.\n')