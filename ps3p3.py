NumberofBooks= float(input("Enter the number of books to order"))
CostPerBook= float(input("Enter the cost per book"))

Total= NumberofBooks * CostPerBook
if Total > 50.00:
  Shipping = 0
else:
  Shipping = 25.00

OrderTotal= Total + Shipping

print("Order Total is $", OrderTotal)
print("Shipping charge is $", Shipping)
