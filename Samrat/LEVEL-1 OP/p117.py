n=int(input('Enter the value of n.\n'))
k=int(input('Enter the value of k.\n'))
for i in range(0,n):
    if k**i>n:
        print(k**(i-1))
        break