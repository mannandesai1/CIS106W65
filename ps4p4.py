NumberofTickets = float(input("Enter the number of tickets"))

if NumberofTickets >= 25:
  PricePerTicket = 50.00
elif NumberofTickets > 10:
  PricePerTicket = 60.00
elif NumberofTickets > 5:
  PricePerTicket = 70.00
else:
  PricePerTicket = 75.00

Total = NumberofTickets * PricePerTicket

print("The number of tickets is", NumberofTickets)
print("The price per ticket is $", PricePerTicket)
print("The total cost is $", Total)
