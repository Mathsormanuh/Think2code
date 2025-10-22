


a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
count=0
for i in range(a,b+1):
    if i%2==0:
        count+=1
print("The count of even numbers is:",count)