p = float(input("Enter Principle"))
r = float(input("Enter Rate"))
totalinterest = 0.0
print("Year          Beginning Balance           Ending Balance")

for x in range (1, 6, 1):
  i = p * r
  totalinterest= totalinterest + i
  endingbalance= p + i
  print(x, "            ",p, "                      ",endingbalance)
  p = endingbalance

print("Total interest earned", totalinterest)