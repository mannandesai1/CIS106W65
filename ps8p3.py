def outdoorprice (MSRP, make, model, ElecVehicleCode):
  if make == "Honda" and model == "Accord":
    percentoffMSRP = 0.10
  elif make == "Toyota" and model == "Rav4":
    percentoffMSRP = 0.15
  elif ElecVehicleCode == "Y":
    percentoffMSRP = 0.30
  else:
    percentoffMSRP = 0.05    

  amount = percentoffMSRP * MSRP
  NewMSRP = MSRP - amount
  tax = NewMSRP * 0.07
  total = NewMSRP + tax
  return total


  
  



response = input("Do you want to know the out the door price of a   car?(Y or N)")
TotalMSRP = 0.0
TotalPrice = 0.0
while response == "Y":
    model = input("Enter the model of the car")
    make = input("Enter make of the car")
    MSRP = float(input("Enter the MSRP price of the car"))
    TotalMSRP = TotalMSRP + MSRP
    ElecVehicleCode = input("Is your car electric?")
    total = outdoorprice (MSRP, make, model, ElecVehicleCode)
    TotalPrice = TotalPrice + total

    print("Total is $: ", total)
    print("Make of Car: ", make)
    print("Model of Car: ", model)
    
  
    response = input("Do you want to know the out the door price of    car?(Y or N)")
print("Total MSRP is $ ", TotalMSRP)
print("Total Price is $ ", TotalPrice)
    