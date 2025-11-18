strng=input('Enter the value of the string.\n')
words=1
lens=len(strng)
for char in strng:
    if char==' ':
        words+=1
    else:
        words=words
print(f'The number of words in the string is {words}') 