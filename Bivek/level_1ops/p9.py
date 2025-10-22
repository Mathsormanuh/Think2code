a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
count=0
for i in range(a,b+1):
    digits=len(str(i))
    if digits%2==0:
        count+=1
print("The count of numbers with even number of digits is:",count)