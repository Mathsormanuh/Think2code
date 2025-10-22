import math
n=int(input("enter the value of n:"))
root=math.isqrt(n)
if root*root==n:
    print("yes")
else:
    print("no")
