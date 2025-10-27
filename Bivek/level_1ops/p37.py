x = int(input("Enter a number: "))
y= int(input("Enter another number: "))
if x==0 and y==0:
    print("Point lies on origin.")
elif x==0:
    print("Point lies on y-axis.")
elif y==0:
    print("Point lies on x-axis.")
else:
    print("Point neither lies in x-axis nor y-axis.")