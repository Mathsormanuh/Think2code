n=int(input('Enter the number of rows.\n'))
alph=ord('a')
for i in range(n):
    for j in range(i):
        print(chr(alph),end='')
        alph=alph+1
    print()
