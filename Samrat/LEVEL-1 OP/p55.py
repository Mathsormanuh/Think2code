n=int(input('Enter the number of rows.\n'))
value=0
for i in range(n):
    for j in range(i):
        print(2*value,end='')
        value+=1
    print()
