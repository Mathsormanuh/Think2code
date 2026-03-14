n=input('Enter the numbers separated by a space.\n')
lst=[int(x) for x in n.split(' ')]
uniq=[]
for x in lst:
    if x not in uniq:
        uniq.append(x)
counter=[]
for x in uniq:
    coun=0
    for y in lst:
        if x==y:
            coun+=1
    counter.append(coun)
for i in range(len(counter)):
    print(f'The frequency of {uniq[i]} is {counter[i]}')
    
