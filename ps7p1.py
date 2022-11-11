def comptotal(quantity, price):
  total = float(quantity) * float(price)


  if total > 10000.00:
    total = total * 0.90
  else:
    total = total

  return total

quantity = float(input("Enter quantity"))
price = float(input("Enter price"))

total = comptotal(quantity, price)
print("Total is $ ", total)
 

                                 