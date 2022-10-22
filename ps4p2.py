PartNumber = float(input("The part number is"))
Quantity = float(input("Enter the quantity"))

if PartNumber == 10 or PartNumber == 55:
  UnitCost = 1.00
elif PartNumber == 99:
  UnitCost = 2.00
elif PartNumber == 80 or PartNumber == 70:
  UnitCost = 3.00
else:
  UnitCost = 5.00

Total = Quantity * UnitCost

print("The part number is", PartNumber)
print("The cost per unit is $", UnitCost)
print("The total is $", Total)