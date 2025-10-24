principal = 1000   
rate = 5           
time = 2           
n = 4              
amount = principal * (1 + rate/(100*n))**(n*time)
compound_interest = amount - principal
print("Principal:", principal)
print("Rate of Interest:", rate, "%")
print("Time (years):", time)
print("Compound Interest:", round(compound_interest, 2))
print("Total Amount:", round(amount, 2))
