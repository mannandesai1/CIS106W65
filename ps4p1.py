Quantity= float(input("Enter the amount of widgets"))

if Quantity > 10000:
  Price = 10.00
elif Quantity > 5000:
  Price = 20.00
else:
  Price = 30.00

ExtendedPrice = Quantity * Price
Tax = ExtendedPrice * 0.07
Total = ExtendedPrice + Tax

print("The Extended Price is $", ExtendedPrice)
print("The tax amount is $", Tax)
print("The total is $", Total)