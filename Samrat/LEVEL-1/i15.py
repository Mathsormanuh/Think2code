ver=True
while ver:
    a=float(input('Enter the co-efficient of x^2.\n'))
    b=float(input('Enter the co-efficient of x.\n'))
    c=float(input('Enter the co-efficient of 1.\n'))
    if a==0:
        print('It is a linear equation. Please enter again.\n')
    else:
        x=round(-b+(b*b-4*a*c)**(1/2))/(2*a)
        y=round(-b-(b*b-4*a*c)**(1/2))/(2*a)
        print('The roots of the quadratic equation are {} and {}.\n'.format(x,y))
        ver=False
