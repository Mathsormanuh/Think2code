str1=input('Enter the first string.\n')
str2=input('Enter the second string.\n')
n1=len(str1)
n2=len(str2)
fact=True
if n1==n2:
    fact=True
else:
    fact=False
for i in range(n1):
    if str1[i] in str2:
        fact=True
    else:
        fact=False
if fact:
    print('The strings are anagram.\n')
else:
    print('The strings are not anagram.\n')
