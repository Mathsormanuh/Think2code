st=input('Enter the values with space.\n')
ls=[int(x) for x in st.split(' ')]
if len(ls)==0:
    print('List is empty.')
elif len(ls)==1:
    print('Mode is one.')
else:
    freq=[]
    uniq=[]
    for x in ls:
        if x not in uniq:
            uniq.append(x)
    for x in uniq:
        count=0
        for y in ls:
            if x==y:
                count=count+1
        freq.append(count)
    max=0
    for x in freq:
        if max<=x:
            max=x
    mode=[]
    for i in range(0,len(freq)):
        if freq[i]==max:
            mode.append(uniq[i])
    if len(mode)==1:
        print(f'The mode is {mode[0]}')
    elif len(mode)==len(uniq):
        print('No mode exists.')
    else:
        print(f'The list of modes are {mode}')