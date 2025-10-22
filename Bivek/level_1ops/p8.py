a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
m=int(input("enter the value of m:"))
s=0
for i in range(a,b+1):
    if i%m==0:
        s=i
if s==0:
    print(-1)
else:
    print("The largest multiple of",m,"between",a,"and",b,"is:",s)
