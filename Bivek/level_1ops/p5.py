a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
k=int(input("enter the value of k:"))
count=0
for i in range(a,b+1):
    if i%k==0:
        count+=1
print("The count of numbers divisible by",k,"is:",count)