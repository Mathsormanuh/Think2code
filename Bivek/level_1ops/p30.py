ch = input("Enter a character: ")
if ch.lower() in 'aeiou':
    print(f"{ch} is a vowel.")
elif ch.upper() in 'AEIOU':
    print(f"{ch} is a vowel.")
else:
    print(f"{ch} is a consonant.")