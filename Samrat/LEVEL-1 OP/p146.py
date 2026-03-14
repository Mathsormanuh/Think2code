st=input('Enter the number with spaces in between.\n')
lst=[int(x) for x in st.split(' ')]
sorlst=sorted(lst)
print(sorlst[::-1])