n=int(input())
a=2
b=1
print(a)
print(b)
for i in range(1,n-1):
    c=a+b
    print(c)
    a=b
    b=c
