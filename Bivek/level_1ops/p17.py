prin_amt=int(input("Enter the principal amount: "))
rate=float(input("Enter the rate of interest: "))
time=int(input("Enter the time in years: "))
simple_interest = (prin_amt * rate * time) / 100
print("The simple interest is:", simple_interest)