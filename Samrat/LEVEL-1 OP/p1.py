n=int(input('Enter the given number.\n'))

p=(n)**(1/2)
r=round(p,0)
#print(p)
#print(r)
if r==p:
    print('The number is a perfect square.\n')
else:
    print('The number is not a perfect square.\n')
