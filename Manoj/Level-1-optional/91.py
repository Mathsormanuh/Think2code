# 91.	Given a and b (a ≤ b), print the count of even numbers in [a, b].

a = int(input("Enter the starting value : "))
b = int(input("Enter the ending value : "))

count = 0
for i in range(a,b+1,1):
  if(i%2 == 0):
    print(i)
    count = count + 1

print("Count is : ",count)
    


