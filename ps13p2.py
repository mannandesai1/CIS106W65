class student:
  def __init__(self, first,last,CreditHours, DistrictCode):
    self.first = first
    self.last = last
    self.CreditHours = CreditHours
    self.email = first + "."+last+"@outlook.com"
    self.DistrictCode = DistrictCode




  def tuition(self):
    if self.DistrictCode == "I":
      tuitionowed = float(self.CreditHours) * 250
    else:
      tuitionowed = float(self.CreditHours) * 500

    return tuitionowed


  
    

emp = student("Mannan","Desai",25,"I")

print(emp.email)
print(emp.first)
print(emp.last)
print(emp.CreditHours)
print(emp.DistrictCode)
print(emp.tuition())


    
   