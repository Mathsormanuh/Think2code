st=input('Enter the number with spaces in between.\n')
lst=st.split(' ')
lst1=sorted(lst)
max=lst1[-1]
fil=[x for x in lst1 if x!=max]
print(fil[-1])