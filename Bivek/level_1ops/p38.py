a = float(input("Enter a number: "))
b= float(input("Enter another number: "))
c= float(input("Enter another number: "))
if a==b==c:
    print("Equilateral triangle.")
elif a==b or b==c or c==a:
    print("Isosceles triangle.")
else:
    print("Scalene triangle.")