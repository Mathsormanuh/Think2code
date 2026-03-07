p=int(input("Enter principal:" ))
t=int(input("enter time:"))
r=int(input("enter rate: "))
amount=p*(1+(r/100))**t
CI=amount-p
print("compound interest =", CI)