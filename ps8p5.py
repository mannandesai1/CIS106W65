def AssessedValue(county, marketvalue):
  if county == "Cook":
    AssessedValuePercent = 0.90
  elif county == "DuPage":
    AssessedValuePercent = 0.80
  elif county == "McHenry":
    AssessedValuePercent = 0.75
  elif county == "Kane":
    AssessedValuePercent = 0.60
  else:
    AssessedValuePercent = 0.70

  Value = marketvalue * AssessedValuePercent
  return Value



response = input("Do you want to calculate the Assessed Value of Home based on county?(Y or N)")
TotalMarketValue = 0.0
TotalAssessedValue = 0.0
while response == "Y":
    county = input("Enter the county: ")
    marketvalue = float(input("Enter market value of your home: "))
    Total = AssessedValue(county, marketvalue)
    TotalMarketValue = TotalMarketValue + marketvalue
    TotalAssessedValue = TotalAssessedValue + Total

    print("Market Value $: ", marketvalue)
    print("Assessed Value $: ", Total)

    response = input("Do you want to calculate the Assessed Value       of Home based on county?(Y or N)")
  

print("Total Market Value $: ", TotalMarketValue)
print("Total Assessed Value $: ", TotalAssessedValue)