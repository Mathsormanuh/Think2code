st=input('Enter the string.\n')
found=False
for char in st:
    if st.count(char)==1:
        print(f'The first non-repeatable character is {char}')
        found=True
        break
if found==False:
    print(f'No non-repeatable letters are found.\n')
    

            