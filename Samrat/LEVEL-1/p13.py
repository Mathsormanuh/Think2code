c=int(input('Enter the value of cost price.\n'))
s=int(input('Enter the value of selling price.\n'))
if c>s:
    l=c-s
    print('The loss is {}'.format(l))
    lp=(l/c)*100
    print('The loss percent is {}%'.format(lp))
else:
    p=s-c
    print('The profit is {}'.format(p))
    pp=(p/c)*100
    print('The profit percent is {}%'.format(pp))
