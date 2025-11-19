def arm():
    n=input('Enter the number.\n')
    length=len(n)
    st=[]
    value=0
    for i in range(length):
        value=int(str(n[i]))**len(n)+value
    if value==int(n):
        print('The number is an armstrong number.\n')
    else:
        print('The number is not an armstrong number.\n')
arm()