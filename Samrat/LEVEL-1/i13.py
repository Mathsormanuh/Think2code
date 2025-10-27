x=int(input('Enter the x coordinate.\n'))
y=int(input('Enter the y coordinate.\n'))
if x==0 and y!=0:
    print('The point is on the y-axis.\n')
elif x==0 and y==0:
    print('The point is on the origin.\n')
elif y==0 and x!=0:
    print('The point is on the x6-axis.\n')
else:
    print('The point is not on the axes.\n')
