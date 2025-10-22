n=int(input("enter the value of n:"))
div=0
for i in range(1,n):
    if n%i==0:
        div+=i
if div==n:
    print("perfect")
elif div>n:
    print("abundant")
else:
    print("deficient")
    
