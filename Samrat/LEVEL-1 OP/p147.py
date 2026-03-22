st=input('Enter the number with spaces in between.\n')
lst=[int(x) for x in st.split(' ')]
sorlst=sorted(lst)
if len(lst)%2==0:
    med=(sorlst[len(lst)/2]+sorlst[len(lst)/2+1])/2
else:
    med=sorlst[int((len(lst)+1)/2)]
print(med)