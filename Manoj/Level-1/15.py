# 15.	Calculate compound interest

principal = float(input("Enter the principal amount : "))
rate = float(input("Enter the rate of interest : "))
time = float(input("Enter the time period : "))
frequency = float (input("Interest compound in a year : "))

future_value = principal * ((1 + rate / frequency)**(frequency * time))

compound_interest = future_value - principal

print("Compound Interest is : ",compound_interest)