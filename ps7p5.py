def comptuitionowed(credithours,districtcode):
  if districtcode == "I":
    tuitionowed = credithours * 250
  else:
    tuitionowed = credithours * 550


  return tuitionowed



lastname = input("Enter Last Name: ")
credithours = float(input("Enter Credit Hours: "))
districtcode = input("Enter District Code: ")
tuitionowed = comptuitionowed(credithours,districtcode)
print("Enter Student Last Name", lastname)
print("Tuition Owed $ ", tuitionowed)



