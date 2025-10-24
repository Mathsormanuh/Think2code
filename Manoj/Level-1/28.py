# 13.	Check if point lies on x-axis, y-axis or origin

x = float(input("Enter the value of x-axis : "))
y = float(input("Enter the value of y-axis : "))

if x==0 and y==0:
  print("Point lies in the origin")
elif y==0:
  print("Point lies in the y-axis")
elif x==0:
  print("Point lies in the x-axis")
else:
  print("The point lies in the coordinate plane")