f = open("data2.txt", "r")
TotalBonus = 0
C = 0
LastName = f.readline()
while LastName != "":
  Salary = f.readline()
  print()
  print("Employee Last Name: ", LastName)
  print("Employee Salary: $", format(float(Salary),
  '10,.2f'))
  Bonus = float(Salary) * 0.10
  print("Employee Bonus: $", format(Bonus, '10,.2f')) 
  TotalBonus = TotalBonus + Bonus
  C = C + 1
  LastName = f.readline()
f.close()
AverageBonus = TotalBonus / C
print(" ")
print("Average Bonus: $", AverageBonus)


      