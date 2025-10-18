P=int(input('Enter the principal.\n'))
r=int(input('Enter the rate of interest.\n'))
t=int(input('Enter the time period.\n'))
A=P*(1+r/100)**t
C=A-P
print('The compound interest is {}'.format(round(C,2)))