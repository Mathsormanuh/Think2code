g=input('Enter the gray code.\n')
b=g[0]
for i in range(1,len(g)):
    if b==g[i]:
        b=b+'0'
    else:
        b=b+'1'
print(f'The binary representation is {b}')
