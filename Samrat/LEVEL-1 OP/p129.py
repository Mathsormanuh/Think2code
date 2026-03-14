#3-bit gray code, input (1-7)
n=int(input())
stir=''
while n!=1:
    stir=str(n%2)+stir
    n=n//2

bi=str(1)+stir
abi='0'+bi[0:len(bi)-1]
gray=''
for i in range(len(bi)):
    if bi[i]==abi[i]:
        gray=gray+'0'
    else:
        gray=gray+'1'

print(gray)