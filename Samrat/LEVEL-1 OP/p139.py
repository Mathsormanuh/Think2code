st=input('Enter the number with spaces in between.\n')
lst=st.split(' ')
max=int(lst[0])
for i in lst:
    if int(i)<=max:
        max=int(i)
print(max)
