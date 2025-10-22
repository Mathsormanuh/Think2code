n=int(input("enter the value of n:"))
div=0
for i in range(1,n):
    if n%i==0:
        div+=i
if div==n:
    print("yes")
else:
    print("no")
