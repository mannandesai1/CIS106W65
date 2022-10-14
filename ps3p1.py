Quantity = float(input("Enter quantity ordered"))

if Quantity>=1000:
   UnitPrice = 3.00
else:
   UnitPrice = 5.00

ExtendedPrice = Quantity * UnitPrice
Tax = ExtendedPrice * 0.07
Total = Tax + ExtendedPrice

print("Quantity Ordered", Quantity)
print("Unit Price $", UnitPrice)
print("Extended Price $", ExtendedPrice)
print("Tax $", Tax)
print("Total $", Total)