months = int(input("Enter the number of months: "))
if months < 0:
    print("Invalid input. Number of months cannot be negative.")
else:
    days = months * 30
    print(f"{months} months is equivalent to {days} days.")