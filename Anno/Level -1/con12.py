month=int(input("enter a month number"))
1=[4,6,9,11]
12=[1,3,5,8,10,12]
if month==2:
    print("28 or 29 days")
elif month in 11:
    print("30 days")
elif month in 12:
    print("31 days")
else:
    print("invalid month")
