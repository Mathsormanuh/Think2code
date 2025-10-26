month=input('Enter the name of the month.\n')
if month in 'February'.lower():
    print('The number of days is 28.\n')
elif month in 'April,June,August,September,November'.lower():
    print('The number of days is 30.\n')
else:
    print('The number of days is 31.\n')

