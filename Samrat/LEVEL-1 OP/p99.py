n=int(input())
a=0
b=0
c=1
print(a)
print(b)
print(c)
for i in range(1,n-2):
    d=a+b+c
    a=b
    b=c
    c=d
    print(d)