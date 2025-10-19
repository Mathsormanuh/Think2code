a=int(input('Enter the first number.\n'))
b=int(input('Enter the second number.\n'))
s=0
for i in range (a,b+1):
    if i==int(str(i)[::-1]):
        s+=1
    else:
        s=s
print('The count of palindrome number is {}'.format(s))