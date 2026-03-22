st=input('Enter the number with spaces in between.\n')
lst=st.split(' ')
max=int(lst[0])
min=int(lst[-1])
for i in lst:
    if int(i)>=max:
        max=int(i)
for i in lst:
    if int(i)<=min:
        min=int(i)

print(max-min)
