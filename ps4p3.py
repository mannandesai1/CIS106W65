PrincipleCD = float(input("Enter principle amount of CD"))
YeartoMaturity = float(input("Enter years to maturity"))

if PrincipleCD > 100000 and YeartoMaturity ==5:
  InterestRate = 0.06
elif PrincipleCD > 50000 and PrincipleCD < 100000 and YeartoMaturity ==10:
  InterestRate = 0.05
elif PrincipleCD > 50000 and PrincipleCD < 100000 and YeartoMaturity ==5:
  InterestRate = 0.04
else:
  InterestRate = 0.02

FirstYearInterest = PrincipleCD * InterestRate

print("The principal is", PrincipleCD)
print("The interest rate is", InterestRate)
print("The interest amount for first year is", FirstYearInterest)