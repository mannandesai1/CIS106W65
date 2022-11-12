def compgrosspay(hours,payrate):
  if hours > 40:
    grosspay = (hours - 40) * payrate * 1.5 + 40 * payrate
  else:
    grosspay = hours * payrate

    return grosspay
  
def comppayrate(jobcode):
    if jobcode == "A":
      payrate = 30.00
    elif jobcode == "L":
      payrate = 25.00
    else:
      payrate = 50.00

    return payrate



lastname = input("Enter your last name")  
jobcode = input("Enter your job code (L, A, J")
hours = float(input("Enter number of hours worked"))
payrate = comppayrate(jobcode)
grosspay = compgrosspay(hours,payrate)
print("Employee Last Name: ", lastname)
print("Employee gross pay is $ ", grosspay)