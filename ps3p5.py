LastName = input("Enter Last Name")
GrossPay = input("Enter your Gross Income")
NumberofAttendents = input("Enter the number of dependents") 

AdjustedGross= float(GrossPay) - 12000.00 * float(NumberofAttendents)

if AdjustedGross > 50000.00:
    tax = AdjustedGross * 0.20
else:
    tax = AdjustedGross * 0.10

if tax < 0:
  tax = 100.00

print("Last Name is ", LastName)
print("Gross Income is $", GrossPay)
print("Number of Dependents",  NumberofAttendents)
print("Adjusted Gross Income is $", AdjustedGross)
print("Income Tax is $", tax)