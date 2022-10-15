item = input("Please enter item (A or B")
Quantity = float(input("Enter quantity ordered"))

if item== "A":
  UnitPrice = 10.00
else:
  UnitPrice = 20.00

ExtendedPrice = Quantity * UnitPrice

print("Item", item)
print("Quantity Ordered", Quantity)
print("Unit Price $", UnitPrice)
print("Extended Price is $", ExtendedPrice)