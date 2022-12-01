def baverage(score1, score2, score3, handicap):
  Sum = score1 + score2 + score3 
  Average = (Sum/3)
  hAverage = (Sum + handicap) / 3
  return Average, hAverage





LastName = str(input("Enter Bowlers Last Name: "))
score1 = float(input("Enter score 1: "))
score2 = float(input("Enter score 2: "))
score3 = float(input("Enter score 3: "))
handicap = float(input("What is your handicap?: "))
Average,hAverage =  baverage(score1, score2, score3, handicap)


print("Last Name: ", LastName)
print("Score Average: ", Average)
print("Handicap Average: ", hAverage)

            