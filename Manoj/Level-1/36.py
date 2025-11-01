#6.	Print Fibonacci series up to n terms

end = int(input("Enter the ending range : "))

a = 0
b = 1

print("Fibonacci series is : ")
for i in range (end):
  print(a,end =" ")
  c = a + b   
  a = b       
  b = c

