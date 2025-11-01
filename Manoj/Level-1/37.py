# 7.	Check if number is prime

n = int(input("Enter the nnumebr you want to check : "))

prime = 0
for i in range(2,n):
  if(n % i == 0):
   prime = 1
   break

if prime == 0:
  print(f"{n} is Prime")
else:
  print(f"{n} is Composite")