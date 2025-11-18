n=int(input('Enter the number of rows.\n'))
for i in range(1,n+1):
    vac=''
    for j in range(1,i+1):
        new=j
        vac=vac+str(new)
    print(' '*(n+1-i)+vac)