row=int(input('Enter the number of rows.\n'))
col=int(input('Enter the number of columns.\n'))
print('*'*row)
for i in range(row-2):
    print('*',end='')
    for j in range(col-2):
        print(' ',end='')
    print('*',end='')
    print()
print('*'*row)