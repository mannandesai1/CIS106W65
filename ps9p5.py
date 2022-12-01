Total = 0.0
Tax = 0.0
def comptotal(quantity, price):
  global Total
  Total = quantity * price
  global Tax
  Tax = Total * 0.07



  return 


quantity = float(input("Enter Quantity: "))
price = float(input("Enter Price Per Unit: $ "))
comptotal(quantity, price)
print("Total is: $ ", Total)
print("Tax cost is: $ ", Tax)