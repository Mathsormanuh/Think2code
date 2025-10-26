s1=float(input('Enter the length of the first side of the triangle.\n'))
s2=float(input('Enter the length of the second side of the triangle.\n'))
s3=float(input('Enter the length of the third side of the triangle.\n'))
if s1==s2==s3:
    print('The triangle is equilateral.\n')
elif s1==s2 or s1==s3 or s2==s3:
    print('The triangle is isosceles.\n')
else:
    print('The triangle is scalene.\n')