# 15.	Print patterns (right triangle, pyramid)

# #Right Triangle
# n = int(input("Enter the end range : "))

# for i in range ( 1 ,n+1 ):
#   print(i * "x")


# Pyramid
n = int(input("Enter the end range : "))

for i in range( 1 , n +1):
  print(" "*(n-i) + "X"* ((2*i) -1))
  