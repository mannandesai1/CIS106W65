LastName = input("Enter Last Name")
Salary = float(input("Enter current salary"))
JobLevel = float(input("Enter job level"))

if JobLevel > 10:
  BonusRate = 0.25
elif JobLevel > 5:
  BonusRate = 0.20
else: 
    BonusRate = 0.10

Bonus = Salary * BonusRate

print("Employee Last name is", LastName)
print("Bonus Rate is", BonusRate)
print("Total Bonus is $", Bonus)
