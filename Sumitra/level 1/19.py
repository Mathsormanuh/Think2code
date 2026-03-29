ch = 'e'
ch = ch.lower()
if ch.isalpha():
    if ch in 'aeiou':
        print(ch, "is a vowel")
    else:
        print(ch, "is a consonant")
else:
    print("Invalid input. Please enter an alphabet.")
