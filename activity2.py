units = float(input("Enter the number of units consumed: "))

# Initialize variables
per_unit_cost = 0
tax = 0

# Determine per-unit cost and tax based on units consumed
if units < 50:
    per_unit_cost = 2.60
    tax = 25
elif 50 <= units < 100:
    per_unit_cost = 3.25
    tax = 35
elif 100 <= units < 200:
    per_unit_cost = 5.26
    tax = 45
else:  # units >= 200
    per_unit_cost = 8.45
    tax = 75

# Calculate total bill
bill_amount = (units * per_unit_cost) + tax

# Display the bill details
print("\n--- Electricity Bill ---")
print(f"Units Consumed: {units}")
print(f"Per Unit Cost: {per_unit_cost}")
print (f"tax:{tax}")
print (f"total Bill Amount:{bill_amount:}")