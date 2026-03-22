st=input()
ls=[int(x) for x in st.split()]
sum=0
for x in ls:
    sum=sum+x
mean=sum/len(st)
var=0
for i in range(len(ls)):
    var+=(ls[i]-mean)**2
print((var/len(ls))**(1/2))