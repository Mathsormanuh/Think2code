st=input('Enter the string.\n')
for char in st:
    if char in 'aeiou':
        st=st.replace(char,"")
print(f'The string without any vowels is {st}')