year=int(input('Enter the year.\n'))
if year%4==0:
    if year%100!=0:
        if year%400==0:
            print('The year is a leap year.\n')
        else:
            print('The year is a century year.\n')
    else:
            print('The year is a leap year.\n')
else:
    print('The year is not a leap year.\n')