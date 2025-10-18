#py87
a =  int(input("Enter the a number : "))

sum=0
for i in range(1,a):
  if a%i==0:
    print("Count is  :",i)
    sum = sum+i

print("Sum is :",sum)
