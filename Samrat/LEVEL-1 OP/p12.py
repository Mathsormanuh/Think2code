value=True
while value:
    a=int(input('Enter the value of a.\n'))
    b=int(input('Enter the value of b.\n'))
    if abs(b-a)<=5:
        value=False
        break
    else:
        print('Enter the values again.\n')
LCM=1
num=b-a+1