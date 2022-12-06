class Employee:
  def __init__(self, first,last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + "."+last+"@outlook.com"




  def mybonus(self,rate):
    bonus = self.pay * rate
    return bonus

emp = Employee("Desai", "Smith", 7000.00)


print(emp.first, "  ", emp.last)
print(emp.pay)
print(emp.email)
print(emp.mybonus(0.10))
print("Bonus is: $", emp.mybonus(0.10)) 
    
   
  