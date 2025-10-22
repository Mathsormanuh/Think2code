a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
k=int(input("enter the value of k:"))
sum=0
for i in range(a,b+1):
    if i%k!=0:
        sum+=i
print("The sum of numbers not divisible by",k,"is:",sum)