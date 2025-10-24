# 7.	Check if triangle is valid

sidea = int(input("Enter the value of side a : "))
sideb = int(input("Enter the value of side b : "))
sidec = int(input("Enter the value of side c : "))

if(sidea + sideb > sidec) and (sidec + sideb > sidea) and (sidea + sidec > sideb):
  print("Valid Triangle")
else:
  print("Invalid")