#12.	Find GCD of two numbers

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

max_number = min(a,b)

for i in range(1,min(a,b)+1):
  if a % i == 0 and b % i == 0:
    gcd = i
    
print(f"The GCD of the number {a} and {b} is {gcd}")