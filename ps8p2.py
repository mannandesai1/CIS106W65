def squarefootage (length, width, height):
  sqaurefootagetotal = 2 * length * width + 2 * length * height + 2 *      width * height
  gallons = sqaurefootagetotal / 50
  return gallons

response = input("Do you want to compute gallons of paint for your room(Y or N)")
while response == "Y":
  length = float(input("Enter length the room"))
  width = float(input("Enter width of the room"))
  height = float(input("Enter height of the room"))
  gallons =  squarefootage (length, width, height)
  print("Number of gallons needed", gallons)
  response = input("Do you want to compute gallons of paint for   your room(Y or N)")

  
  