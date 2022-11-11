lastname= input("Enter Player Last Name")
hits= input("Enter Number of Hits")
atbats = input("Enter Number At Bat")

def compavg(hits,atbats):
  average = float(hits) / float(atbats)


  return average
average = compavg(hits,atbats)
print("Player Last Name: ", lastname)
print("Batting Average: ", average)
  

  

  
    


