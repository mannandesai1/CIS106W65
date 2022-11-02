f = open("data1.txt", "r")

C = 0.0
TotalTuition = 0.0

#get first part of data 
LastName = str(f.readline().rstrip('\n'))


while LastName != "":
  DistrictCode = str(f.readline().rstrip('\n'))
  Credits = float(f.readline())
  
  if DistrictCode == "I":
    CostPerCredit = 250.00
  else:
    CostPerCredit = 500.00

  Tuition = CostPerCredit * Credits
  C = C + 1
  TotalTuition = TotalTuition + Tuition

  print("Student",  LastName)
  print("Credits Taken:",  Credits)
  print("Tuition Owed:",   Tuition )

  LastName = str(f.readline().rstrip('\n'))

f.close()
print("Number of Students", C)
print("Total Tuition Owed",  TotalTuition )
  