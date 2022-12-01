def examaverage (exam1, exam2, exam3):
  Sum = exam1 + exam2 + exam3
  Total = 300
  Percentage = (Sum/Total) * 100
  Average = (Sum/3)
  Points = exam1 + exam2 + exam3

  return Average, Points




LastName = str(input("Enter Last Name: "))
exam1 = float(input("Enter score for Exam 1: "))
exam2 = float(input("Enter score for Exam 2: "))
exam3 = float(input("Enter score for Exam 3: "))


Average,Points = examaverage (exam1, exam2, exam3)
print("Last Name: ", LastName)
print("Exam Score Average: ", Average)
print("Total Points: ", Points)