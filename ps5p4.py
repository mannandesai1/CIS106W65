Response = input("Do you want to work over 40 hours to earn time and a half(Yes or No)")
SumGrossPay = 0
NumberofEmployees = 0
while Response == "Yes":
  LastName = input("Enter Last Name")
  HoursWorked = float(input("Enter Hours Worked"))
  Rate = float(input("Enter Hourly Rate"))

  if HoursWorked > 40:
    GrossPay = (Rate * 40) + (HoursWorked - 40) * 1.5 * Rate
  else:
    GrossPay = Rate * HoursWorked
  
  print("Gross Pay is $", GrossPay)
  SumGrossPay = SumGrossPay + GrossPay
  NumberofEmployees = NumberofEmployees + 1

  Response = input("Do you want to work over 40 hours to earn time and a half(Yes or No)")

AverageGrossPay = SumGrossPay / NumberofEmployees

print("Sum of all gross pay is $", SumGrossPay)
print("Number of Employees is", NumberofEmployees)
print("The average gross pay is $", AverageGrossPay)