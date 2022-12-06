def loadarrays(LastName1, salaries):
  f = open("myfile.txt", "r")
  for i in range (0,10,1):
    LN = f.readline()
    LN = LN.rstrip("\n")
    LastName1.append(LN)
    s = f.readline()
    s.rstrip("\n")
    salaries.append(float(s))
  f.close()
def darrays(LastName, salaries):
  for i in range (0,10,1):
      print (LastName1[i], "salary is: ", salaries[i])
def hilow(LastName, salaries):
   hiscore = 0.0
   hisub = 0
   lowscore = 999999.00
   lowsub = 0
   
   for i in range (0,10,1):
     if salaries[i] > hiscore:
          hiscore = salaries[i]
          hisub = i
     if salaries[i] < lowscore:
         lowscore = salaries[i]
         lowsub = i

   print(LastName[hisub], "has highest salary of ",   
   salaries[hisub])
 
   print(LastName[lowsub], "has lowest salary of ",                      salaries[lowsub])

def displayarrays(LastName,salaries):
    for i in range (0,10):
      print (LastName[i], "has salary of: ", salaries[i])
  





def rdisplay(LastName):
      for i in range (9,-1,-1):
        print(LastName[i])



      print(LastName)
      LastName.reverse()
      print(LastName)

LastName = ["Adams", "Desai", "Smith", "Patel", "Davis", "Jones", "James", "Jordan", "Johnson", "Bird"]
salaries = [50000.00, 35000.00, 5000.00, 60000.00, 30000.00, 45000.00, 25000.00, 75000.00, 80000.00, 15000.00]



#displayarrays(LastName, salaries)
#print("Reverse Order")
#rdisplay(LastName)
LastName1 = []
salaries = []

loadarrays(LastName1, salaries)
darrays(LastName1, salaries)
hilow(LastName, salaries)
