a=int(input("enter the value of a:"))   
b=int(input("enter the value of b:"))
num=0
max_digit=-1
for i in range(a,b+1):
    digit=sum(int(d) for d in str(i))
    if digit>max_digit:
        max_digit=digit
        num=i
print("The number with maximum digit sum is:",num)
print("The maximum digit sum is:",max_digit)
