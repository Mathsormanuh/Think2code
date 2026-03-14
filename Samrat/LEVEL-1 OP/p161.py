n=input('Enter the number separated by space.\n')
lst=[int(x) for x in n.split(' ')]
even=[]
odd=[]
for x in lst:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)

print(even)
print(odd)