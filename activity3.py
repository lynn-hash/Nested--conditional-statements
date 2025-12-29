print("Welcome to Ride Selector!")
print("Select a category:")
print("1. Bike")
print("2. Car")

# Get user's main category choice
category_choice = input("Enter 1 for Bike or 2 for Car: ")

# Initialize variable for ride choice
ride = ""

# Check category and display subcategories
if category_choice == "1":
    print("\nYou selected Bike. Choose a type:")
    print("a. Sports Bike")
    print("b. Cruiser Bike")
    sub_choice = input("Enter a for Sports Bike or b for Cruiser Bike: ")
    if sub_choice.lower() == "a":
        ride = "Sports Bike"
    elif sub_choice.lower() == "b":
        ride = "Cruiser Bike"
    else:
        print("Invalid choice for bike.")
elif category_choice == "2":
    print("\nYou selected Car. Choose a type:")
    print("a. Sedan")
    print("b. SUV")
    sub_choice = input("Enter a for Sedan or b for SUV: ")
    if sub_choice.lower() == "a":
        ride = "Sedan"
    elif sub_choice.lower() == "b":
        ride = "SUV"
    else:
        print("Invalid choice for car.")
else:
    print("Invalid main category choice.")

# Display final selection
if ride:
    print(f"\nYou have selected: {ride}")