n=int(input('Enter the height of the diamond.\n'))
print('  '+'*'*(2*(n-2)-1)+' ')
for i in range(n-1,1,-1):
    print(' '*(n-i)+'*'+' '*(2*i-3)+'*'+' '*(n-i))
print(' '*(n-1)+'*'+' '*(n-2))