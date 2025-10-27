n=int(input('Enter the value of n.\n'))
for p in range (2, n+1):
    value=True
    for i in range (2,p):
        if p%i==0:
            value=False
            break
    if value:
        print(p)


        
