n=input('Enter the number separated by space.\n')
lst=[int(x) for x in n.split(' ')]
count=0
uniq=[]
for x in lst:
    if x!=0:
        uniq.append(x)
        count+=1
for i in range(count-1):
    uniq.append(0)

print(uniq)