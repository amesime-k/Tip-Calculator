
print("Welcome to the tip calculator")
total_bill = float(input("What is your total bill? $"))
tip = float(input("What percentage of tip would you like to give? 10,12, or 15? "))
bill_split =float(input("How many people to spilt the bill? "))
calculated_tip = round((total_bill / bill_split) * (1 + (tip / 100)),2) 

# A more detailed calculation of the tip will be added later
print(f"Each person should pay ${calculated_tip}")