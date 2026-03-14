st=input('Enter the number with spaces in between.\n')
lst=st.split(' ')
lst1=sorted(lst)
min=lst1[0]
fil=[x for x in lst1 if x!=min]
print(fil[0])