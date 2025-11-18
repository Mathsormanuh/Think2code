n=int(input('Enter the ending number of Floyds triangle.\n'))
value=1
for i in range(1,n+1):
    print('')
    for j in range(1,i):
        print(value,end='')
        value+=1