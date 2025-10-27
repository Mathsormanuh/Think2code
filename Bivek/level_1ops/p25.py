prin_amount=float(input("Enter the principal amount: "))
rate_of_interest=float(input("Enter the rate of interest: "))
time_period=float(input("Enter the time period in years: "))
compound_interest= prin_amount * ( (1 + rate_of_interest / 100) ** time_period ) - prin_amount
print("The compound interest is:", compound_interest)