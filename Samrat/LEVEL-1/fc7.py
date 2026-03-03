def mult():
    i=int(input('Enter the number for which the table is to be made.\n'))
    n=int(input('Enter the number of rows.\n'))
    for j in range(1,n+1):
        print(f'{i}*{j}='+str(i*j))
mult()