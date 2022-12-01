def discount(quantity, price, discountrate):
  Total = quantity * price
  discountamount = discountrate * Total
  discountprice = Total - discountamount

  return discountamount, discountprice







quantity = float(input("Enter the quantity: "))
price = float(input("Enter the unit price: $ "))
discountrate = float(input("Enter the discount rate: % "))
discountamount,discountprice = discount(quantity, price, discountrate)

print("Quantity: ", quantity)
print("Unit Price: $ ", price)
print("Discounted Amount: $ ", discountamount)
print("Discounted Price: $ ", discountprice)