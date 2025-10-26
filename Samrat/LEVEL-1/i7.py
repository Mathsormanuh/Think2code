s1=float(input('Enter the length of the first side of the triangle.\n'))
s2=float(input('Enter the length of the second side of the triangle.\n'))
s3=float(input('Enter the length of the third side of the triangle.\n'))
if s1+s2>s3 and s2+s3>s1 and s3+s1>s2:
    print('The triangle is valid.\n')
else:
    print('The triangle is not valid.\n')
