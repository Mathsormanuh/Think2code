# 2.	Find largest of three numbers

a = int(input("Enter the number of a : "))
b = int(input("Enter the number of b : "))
c = int(input("Enter the number of c : "))

if(a>b and a>c):
  print("a is greatest")
elif(b>a and b>c):
  print("b is greatest")
else:
  print("c is greatest")