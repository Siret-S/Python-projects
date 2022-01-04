print("Welcome to the tip calculator!")
bill = float(input("What was the total of pill? $"))
tip = int(input("What percentage tip would ypu like to give? 10, 12, or 15? "))
people =int(input("How many people to split the bill? "))

tip_precent = tip / 100
total_tip = bill * tip_precent
total_bill = bill + total_tip
bill_per_person = total_bill / people
share = round(bill_per_person,2)

print(f"Each person should pay: €{share}")