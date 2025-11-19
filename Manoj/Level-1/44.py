# 14.	Print all prime numbers between 1 to n

n = int(input("Enter the end number : "))

print(f"Prime number from 1 to {n} are : ")

for i in range (2,n+1):
  for j in range(2,i):
    if i % j == 0:
      break
  else:
    print(i)
    
  
