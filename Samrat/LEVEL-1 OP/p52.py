n=int(input('Enter the number of rows.\n'))
aleph=ord('a')
for i in range(n+1):
    for j in range(i):
        print(chr(aleph),end='')
        aleph+=1
    print()