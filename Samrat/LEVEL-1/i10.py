elec=int(input('Enter the units of electricity used.\n'))
print('For the first 100 units the cost per unit is 50')
print('For the second 100 units the cost per unit is 80')
print('After that the cost per unit is 100')

if elec>200:
    print('The electricity bill is {}'.format((elec-200)*100+(100)*80+100*50))
elif elec>100:
    print('The electricity bill is {}'.format((elec-100)*80+100*50))
else:
    print('The electricity bill is {}'.format(elec*50))