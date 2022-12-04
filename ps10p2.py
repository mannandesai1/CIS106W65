def displayarrays(LastName, ExamScores):
    for i in range (0,10):
      print (LastName[i], "exam score is: ", ExamScores[i])
  





def rdisplay(LastName):
      for i in range (9,-1,-1):
        print(LastName[i])



      print(LastName)
      LastName.reverse()
      print(LastName)

LastName = ["Adams", "Desai", "Smith", "Patel", "Davis", "Jones", "James", "Jordan", "Johnson", "Bird"]
ExamScores = [95, 90, 85, 72, 88, 100, 90, 89, 95, 80]



displayarrays(LastName, ExamScores)
print("Reverse Order")
rdisplay(LastName)
