# 15.	Calculate roots of quadratic equation

import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

D = (b**2) - (4*a*c)

if D>0:
  root1 = (-b + math.sqrt(D)) / (2*a)
  root2 = (-b - math.sqrt(D)) / (2*a)
  print(f"The roots are real and distinct: {root1} and {root2}")

elif D==0:
  root1 = root2 = -b / (2*a)
  print(f"The roots are real and distinct: {root1} and {root2}")

elif D<0:
  real = -b / (2*a)
  imag = math.sqrt(abs(D)) / (2*a) #abs = absolute value i.e (-2)=2
  print(f"The roots are complex: {real}+{imag}i and {real}-{imag}i")