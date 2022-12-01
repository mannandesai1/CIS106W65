def salesreport (sales):
  if sales > 100000.00:
    per = 0.10

  elif sales <= 100000.00:
    per = 0.05
  commission = sales * per
  nextyear = sales * 1.05
  return commission, nextyear


SalesPerson = input("Enter Sales Person Name: ")
LastName = input("Enter Last Name: ")
sales = float(input("Enter Sales Amount: "))
commission,nextyear = salesreport (sales)

print("Commision: $ ", commission)
print("Next Years Report: ", nextyear)