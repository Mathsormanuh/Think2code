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
print('The required numbers are:\n')
reqd=[]
for i in range(len(counter)):
    if counter[i]!=1:
        reqd.append(uniq[i])
print(reqd)
