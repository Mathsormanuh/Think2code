n=int(input('Enter the number of rows.\n'))
value=0
for i in range(n):
    for j in range(i):
        print(value*2+1,end='')
        value+=1
    print()