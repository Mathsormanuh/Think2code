# 6.	Calculate grade based on marks

marks = int(input("Enter the student marks : "))

if marks >= 90:
  grade = 'A'
elif marks >= 80:
  grade = 'B'
elif marks >= 70:
  grade = 'C'
elif marks >= 60:
  grade = 'D'
else:
  grade = 'F'

print("Grade:", grade)