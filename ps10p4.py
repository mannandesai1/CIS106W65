def loadarrays(LastName, BattingAverage):
  f = open("myfile.txt", "r")
  for i in range (0,10,1):
    LN = f.readline()
    LN = LN.rstrip("\n")
    LastName.append(LN)
    s = f.readline()
    s = s.rstrip("\n")
    BattingAverage.append(float(s))
  f.close()

def darrays(LastName, BattingAverage):
  for i in range (0,10,1):
      print(LastName[i], "has a batting average of: ", 
      BattingAverage[i])

def SearchLName(LastName1, BattingAverage, LastName):
  c = 5
  for i in range (0,10,1):
      if LastName1 == LastName[i]:
        print(LastName[i], "has a batting average of: ", 
        BattingAverage[i])
        c = 0
  if c == 5:
    print("Player not in the list")
    
            
        


      
      

LastName = []
BattingAverage = []


loadarrays(LastName, BattingAverage)
darrays(LastName, BattingAverage)

response = input("Do you want to enter a players last name (Y or N)")
while response == "Y":
  LastName1 = input("Enter Last Name")
  SearchLName(LastName1, BattingAverage, LastName)
  response = input("Do you want to enter a players last name (Y or N)")


