a=float(input("Enter a number: "))
b=float(input("Enter another number: "))
c=float(input("Enter another number: "))
if a+b>c and b+c>a and c+a>b:
    print("The numbers can form a triangle.")
else:
    print("The numbers cannot form a triangle.")