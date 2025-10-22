a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
s=0
for i in range(a,b+1):
    s+=i*i
print("The sum squares of numbers from",a,"to",b,"are:",s)

