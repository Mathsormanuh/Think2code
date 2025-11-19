def prime():
    n=int(input('Enter the number.\n'))
    iter=True
    for i in range(2,n):
        if n%i==0:
            iter=False
            break
    if iter:
        print('The number is prime.\n')
    else:
        print('The number is not prime.\n')
prime()