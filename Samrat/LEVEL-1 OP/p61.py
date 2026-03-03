n=int(input('Enter the number of rows.\n'))
value=1
for i in range(n+1):
    for k in range(i):
        print(value,end='')
        value+=1
    value=value+1-i
    print()