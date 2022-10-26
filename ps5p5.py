Response = input("Do you want to calculate total order with discount? (Yes or No)")
SumDiscount = 0
Count = 0
while Response == "Yes":
  Quantity = float(input("Enter the quantity of the item"))
  Price = float(input("Enter the price of the item"))
  ExtendedPrice= Quantity * Price

  if ExtendedPrice > 10000.00:
    Discount = ExtendedPrice * 0.25
  else:
    Discount = ExtendedPrice * 0.10

  Total = ExtendedPrice - Discount

  SumDiscount= SumDiscount + Discount
  Count = Count + 1

  print("The Extended Price is $", ExtendedPrice)
  print("The Discount Amount is", Discount)
  print("The total is $", Total)

  Response = input("Do you want to calculate total order with discount? (Yes or No)")

AverageDiscount = SumDiscount / Count

print("The Average Discount is", AverageDiscount)
print("The Total Discount is", SumDiscount)