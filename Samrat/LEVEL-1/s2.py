string=input('Enter the string.\n')
n=len(string)
vowel=0
const=0
for i in range(n):
    if string[i] in 'aeiou':
        vowel=vowel+1
    else:
        const=const+1
print(f'The number of consonants is {const} and the number of vowels is {vowel}')