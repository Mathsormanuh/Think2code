def fact():
    n=int(input('Enter the number for which the factorial is to be found.\n'))
    fact=1
    for i in range(n,1,-1):
        fact=fact*i
    print(f'The required factorial is {fact}')
fact()