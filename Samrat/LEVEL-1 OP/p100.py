n=int(input())
a=1
b=1
c=1
print(a)
print(b)
print(c)
for i in range(1,n-2):
    d=a+b
    print(d)
    a=b
    b=c
    c=d

