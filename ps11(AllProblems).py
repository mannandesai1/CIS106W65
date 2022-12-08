def d11 (mylist):
  n = int(input("Number of items in your list"))
  for n in range (0,n,1):
    s = int(input("Enter an integer"))
    mylist.append(s)
  return mylist
def displaylist(mylist):
  for item in mylist:
      print (item)


#main
mylist = []
mylist = d11(mylist)
displaylist(mylist)
print(mylist)

#DLPorblem2
mylist.insert(0,99)
print(mylist)

#DLProblem3
mylist[0] = 100
print(mylist)

#DLProblem4
mylist2 = ["500", "600", "700", "800", "900"]
mylist.extend(mylist2)
print(mylist2)

#DLProblem5
mylist2.remove("800")
print(mylist2)

#DLProblem6 
mylist2.remove("700")
print(mylist2)

#DLProblem7
mylist3 = ["A", "B", "C", "A", "A", "C"]

#DLProblem8
print("A Grades:  ",mylist3.count ("A"))

#DLProblem9
print("B Grade: ", mylist3.index("B"))

#DLProblem10
look_for = "F"
if look_for in mylist3:
  print(str(look_for) + " is at index " +     
  str(mylist3.index(look_for)))
else:
  print(str(look_for) + " isn't in the list.")

 #DLProblem11
mylist2.clear()
print(mylist2)

#DLProblem12
#del mylist2
#print(mylist2)

#DLProblem13
mylist4 = ["Rizzo", "Davis", "Baez", "Happ","Bryan"]

#DLProblem14
mylist4.sort()
print(mylist4)

#DLProblem15
backwardnames = mylist4.copy()

#DLProblem16
backwardnames.reverse()
print(mylist4)
print(backwardnames)
