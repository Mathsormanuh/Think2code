n=int(input('Enter the height of the triangle.\n'))
alph=ord('A')
for i in range(1,n+1):
    print(' '*(n-i),end='')
    for j in range(1,2*i):
        print(chr(alph),end='')
        alph+=1
    print()