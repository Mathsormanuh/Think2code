a=int(input('Enter the first number.\n'))
b=int(input('Enter the second number.\n'))
maxlength=0
maxnum=a
for i in range (a,b+1):
    s=sum(int(d) for d in str(i))
    if s>maxlength:
        maxlength=s
        maxnum=i
    elif s == maxlength and i < maxnum:
        maxnum = i
print(f"The number with maximum sum of digits is {maxnum}")
print(f"The maximum sum of digits is {maxlength}")