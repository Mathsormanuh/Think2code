# 9.	Check if character is alphabet, digit or special character

a = input("Enter a character: ")

if a.isalpha():
    print("Alphabet")
elif a.isdigit():
    print("Digit")
else:
    print("Special Character")