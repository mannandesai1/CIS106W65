def nextmonthforcast(month,sales):
  if month == "Jan" or month == "Feb" or month == "Mar":
    forcastpercent = 0.10
  elif month == "Apr" or month == "May" or "Jun":
    forcastpercent = 0.15
  elif month == "Jul" or month == "Aug" or month == "Sep":
    forcastpercent == 0.20
  else:
    forcastpercent = 0.25
    
  fsales = sales * (forcastpercent + 1)
  return fsales

response = input("Do you want to calculate next month's sale (Y or N)")
while response == "Y":
  lastname = input("Enter Last Name")
  month = input("Enter Month")
  sales = float(input("Enter sale amount"))
  nextmonthsales = nextmonthforcast(month,sales)
  print("Student Last Name: ", lastname)
  print("Next Month's Forcast: ", nextmonthsales )  
  response = input("Do you want to calculate next month's sale (Y     or N)")
  
  






  