h=int(input('Enter the height of the triangle.\n'))
def com(n,r):
    if n==0:
        ft='1 '
        return ft
    else:
        nfct=1
        rfct=1
        kfct=1
        for i in range(1,n+1):
            nfct=nfct*i
        for i in range(1,r+1):
            rfct=rfct*i
        for i in range(1,n-r+1):
            kfct=kfct*i
        nCr=(nfct)/(rfct*kfct)
        return int(nCr)
for i in range(0,h):
    print(' '*(h-i),end='')
    for j in range(0,i+1):
        print(str(com(i,j)),end='')
    print()