def prime():
    prm=int(input('Enter the number.\n'))
    value=True
    for i in range(2,prm):
        if prm%i==0:
            value=False
            break
    if value:
        print('Yes')
    else:
        print('No')
prime()