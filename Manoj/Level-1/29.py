# 14.	Check if triangle is equilateral, isosceles or scalene

x = float(input("Enter the value of side x : "))
y = float(input("Enter the value of side y : "))
z = float(input("Enter the value of side z : "))

if (x + y > z) and (x + z > y) and (y + z > x):
  if x==y==z:
    print("Equilateral Triangle ")
  elif x==y or y==z or z==x:
    print("Isoceles Triangle")
  elif x!=y!=z:
    print("Scalene Triangle")

else:
  print("Invalid Triangle")