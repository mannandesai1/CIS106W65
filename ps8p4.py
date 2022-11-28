def trainticketprice (milesfromdowntownchicago):
  if milesfromdowntownchicago >= 30:
    ticketprice = 12.00
  elif milesfromdowntownchicago >=20:
    ticketprice = 10.00
  elif milesfromdowntownchicago >=10:
    ticketprice = 8.00
  else:
    ticketprice = 5.00

    
  return ticketprice



response = input("Do you want to caluclate train price based on distance?(Y or N)")
alltickets = 0.0
while response == "Y":
    lastname = input("Enter Last Name: ")
    milesfromdowntownchicago = float(input("Enter miles from            Downtown Chicago: "))
    totalticketprice = trainticketprice (milesfromdowntownchicago)
    alltickets = alltickets + totalticketprice

    print("Last Name: ", lastname)
    print("Ticket Price $: ", totalticketprice)
  
    response = input("Do you want to caluclate train price based on     distance?(Y or N)")

print("Total Ticket Price is $: ", alltickets)