a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
count=0
for i in range(a,b+1):
    s=str(i)
    if s==s[::-1]:
        count+=1
print("The count of palindromic numbers is:",count)