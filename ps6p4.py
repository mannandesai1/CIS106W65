f = open("p4d.txt", "r")

#initialize counter and sums to 0 
C = 0.0
TotalEP = 0.0

#get first data line 
item = str(f.readline().rstrip('\n'))

while item != "":
  quantity = float(f.readline())
  price = float(f.readline())

  ExtendedPrice = quantity * price
  TotalEP = TotalEP + ExtendedPrice
  C = C + 1



  print("Item is:     ",            item)
  print("Quantity is: ",          quantity)
  print("Price is:    ",             price)
  print("Extended Price is      ", ExtendedPrice)


  item = str(f.readline().rstrip('\n'))


print("Total Extended Prices:       ", TotalEP)
print("Number of Orders:            ", C)
Average = TotalEP / C
print("Average Order                ", Average)
  
