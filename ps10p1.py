def displayarrays(LastName):
    for i in range (0,10):
      print (LastName[i])
  





def rdisplay(LastName):
      for i in range (9,-1,-1):
        print(LastName[i])

LastName = ["Adams", "Desai", "Smith", "Patel", "Davis", "Jones", "James", "Jordan", "Johnson", "Bird"]

displayarrays(LastName)
print("Reverse Order")
rdisplay(LastName)
