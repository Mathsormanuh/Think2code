# Calculate BMI (Body Mass Index)

# Assign weight in kilograms and height in meters
weight = 70      # in kg
height = 1.75    # in meters

# Calculate BMI
bmi = weight / (height ** 2)

# Display result
print("Weight:", weight, "kg")
print("Height:", height, "m")
print("BMI:", round(bmi, 2))

# Optional: BMI category
if bmi < 18.5:
    print("Category: Underweight")
elif 18.5 <= bmi < 24.9:
    print("Category: Normal weight")
elif 25 <= bmi < 29.9:
    print("Category: Overweight")
else:
    print("Category: Obese")
