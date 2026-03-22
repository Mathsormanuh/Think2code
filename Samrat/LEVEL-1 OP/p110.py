def fac(n):
    if n==0 or n==1:
        prod=1
    else:
        prod=1
        for i in range(1,n+1):
            prod=prod*i
    return prod

N=int(input('Enter the number of numbers.\n'))
print('Enter the numbers separated by a space.\n')
st=input('')
ls=list(st.split(' '))
pro=1
sum=0
for item in ls:
    sum=sum+int(item)
    pro=pro*fac(int(item))

print(int(fac(int(sum))/(pro)))

