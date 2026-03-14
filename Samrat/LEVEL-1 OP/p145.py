st=input('Enter the number with spaces in between.\n')
lst=[int(x) for x in st.split(' ')]
print(sorted(lst))