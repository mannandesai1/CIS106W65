Counter = 0 
TotalExam1 = 0.0
Response = input("Do you want to calculate average exam score (Yes or No)")

while Response == "Yes":
  Counter = Counter + 1
  LastName = input("Enter student last  name")
  Score1 = float(input("Enter score for Exam 1"))
  Score2 = float(input("Enter score for Exam 2"))
  Average = (Score1+ Score2) / 2
  print(LastName, "has average of", Average)
  TotalExam1 = TotalExam1 + Score1
  Response = input("Do you want to calculate average exam score (Yes or No)")

AverageExam1 = TotalExam1 / Counter
print("Number of Students", Counter)
print("Average Exam Score 1", AverageExam1)