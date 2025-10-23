cost_price = 500
selling_price = 600
if selling_price > cost_price:
    profit = selling_price - cost_price
    profit_percent = (profit / cost_price) * 100
    print("Profit:", profit)
    print("Profit Percentage:", round(profit_percent, 2), "%")
elif selling_price < cost_price:
    loss = cost_price - selling_price
    loss_percent = (loss / cost_price) * 100
    print("Loss:", loss)
    print("Loss Percentage:", round(loss_percent, 2), "%")
else:
    print("No profit, no loss")
