city = input("Enter City: ")
miles = float(input("Enter Miles Travelled "))
gallons = float(input("Enter gallons used "))


def compMPG(miles,gallons):
  MPG = float(miles) / (gallons)

  return MPG


def compcost(gallons):
  costoftrip = gallons * 2.50

  return costoftrip


MPG = compMPG(miles,gallons)
costoftrip = compcost(gallons)

print("Destination City ", city)
print("Total Miles: ", miles)
print("Total Gallons: ", gallons)
print("Total Cost $: ", costoftrip)