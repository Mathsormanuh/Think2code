a=float(input("enter coefficient a: "))
b=float(input("enter coefficient b: "))
c=float(input("enter coefficient c: "))
d=b**2-4*a*c
if d>0:
  root1=(-b+d**0.5)/(2*a)
  root2=(-b-d**0.5)/(2*a)
  print(f"Two real roots exist: {root1} and {root2}")
elif d==0:
  root1=root2=(-b)/(2*a)
  print(f"One real root exists: {root1}")
else:
  print("No real roots exist.")