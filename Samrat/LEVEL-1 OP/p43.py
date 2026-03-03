n=int(input('Enter the number of rows.\n'))
if n%2!=0:
    for i in range(int((n-1)/2)):
        for j in range(0,i):
            print(' ',end='')
        print('*',end='')
        for j in range(n-2*i-2,0,-1):
            print(' ',end='')
        print('*',end='')
        print()
    print(' '*int((n-1)/2)+'*')
    for i in range(int((n-3)/2),-1,-1):
        for j in range(0,i):
            print(' ',end='')
        print('*',end='')
        for j in range(n-2*i-2,0,-1):
            print(' ',end='')
        print('*',end='')
        print()
else:
    for i in range(int(n/2)):
        for j in range(0,i):
            print(' ',end='')
        print('*',end='')
        for j in range(n-2*i-2,0,-1):
            print(' ',end='')
        print('*',end='')
        print()
    for i in range(int((n-2)/2),-1,-1):
        for j in range(0,i):
            print(' ',end='')
        print('*',end='')
        for j in range(n-2*i-2,0,-1):
            print(' ',end='')
        print('*',end='')
        print()