def bin(n):
    stir=''
    while n!=1:
        stir=str(n%2)+stir
        n=n//2
    return str(1)+stir

nb=input()
mb=input()

if len(nb)>len(mb):
    mb='0'*(len(nb)-len(mb))+mb
elif len(nb)<len(mb):
    nb='0'*(len(mb)-len(nb))+nb

coun=0
for i in range(len(nb)):
    if nb[i]!=mb[i]:
        coun+=1

print(coun)