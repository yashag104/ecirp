print("Welcome to the tip calculator.")
bill=float(input("What was the total bill?"))
tip=float(input("What percentage tip would you like to give? 10, 12 pr 15"))
tip=tip/100
person=int(input("How many people to split the bill?"))
f_bill=float(bill+bill*tip)
f_bill=round(f_bill,2)
p_bill=float(f_bill/person)
print(f"Each person should pay:{p_bill}")