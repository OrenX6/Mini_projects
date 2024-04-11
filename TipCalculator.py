print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

bill_per_person = (bill / people) * (1 + (tip / 100))

# final_amount= round(bill_per_person, 2)

final_amount = "{:.2f}".format(bill_per_person)  # more accurate (creating a string using format function)
print(type(final_amount))

print(f"Each person should pay: ${final_amount}")






