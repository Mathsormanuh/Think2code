a1=int(input('Enter English marks.\n'))
a2=int(input('Enter Maths marks.\n'))
a3=int(input('Enter SST marks.\n'))
a4=int(input('Enter Science marks.\n'))
a5=int(input('Enter MIL marks.\n'))
a6=int(input('Enter Elective marks.\n'))
total=a1+a2+a3+a4+a5+a6
percent=total/6
if percent > 90:
    print('The grade is O.')
elif percent > 80:
    print('The grade is A.')
elif percent > 70:
    print('The grade is B.')
elif percent > 60:
    print('The grade is C.')
elif percent > 30:
    print('The grade is D.')
else:
    print('The grade is F.')