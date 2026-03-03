n=int(input('Enter the number of rows.\n'))
alph=ord('a')
for i in range(n):
    for k in range(n-i):
        print(' ',end='')
    for j in range(2*i-1):
        print(chr(alph),end='')
        alph+=1
    print()
for i in range(2*n-1):
    print(chr(alph),end='')
    alph+=1
print()    
for i in range(n-1,0,-1):
    for k in range(n-i):
        print(' ',end='')
    for j in range(2*i-1):
        print(chr(alph),end='')
        alph+=1
    print()