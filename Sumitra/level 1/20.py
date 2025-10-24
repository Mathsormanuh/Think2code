marks = 78
if marks >= 90 and marks <= 100:
    grade = 'A+'
elif marks >= 80:
    grade = 'A'
elif marks >= 70:
    grade = 'B'
elif marks >= 60:
    grade = 'C'
elif marks >= 50:
    grade = 'D'
elif marks >= 0:
    grade = 'F'
else:
    grade = 'Invalid marks'

print("Marks:", marks)
print("Grade:", grade)
