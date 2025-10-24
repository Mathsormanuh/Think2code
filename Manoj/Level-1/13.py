# 13.	Calculate profit or loss percentage

cost = float(input("Enter the cost price : "))
sell = float(input("Enter the selling price : "))

if(sell>cost):
  profit = sell - cost
  profit_percent = (profit/cost)* 100
  print("Profit is : ",profit_percent)
elif(cost>sell):
  loss = cost - sell
  loss_percent = (loss/cost)*100
  print("Loss is : ",loss_percent)

else:
  print("NO profit NO loss") 