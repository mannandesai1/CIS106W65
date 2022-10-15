Appliance= input("Enter the type of appliance")
Cost= float(input("Enter the cost of the appliance"))


if Cost > 1000.00:
  Warrantee = Cost * 0.10
else:
  Warrantee = Cost * 0.05

  Total = Cost + Warrantee

print("The appliance is", Appliance)
print("The cost of the appliance is $", Cost)
print("The cost of the warrantee is $", Warrantee)
print("The total cost is $", Total)