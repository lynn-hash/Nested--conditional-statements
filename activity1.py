medical_cause = input("Do you have a medical cause? (Y/N): ").strip().upper()

if medical_cause == 'Y':
    print("You are allowed to take the exam.")
elif medical_cause == 'N':
    # If no medical cause, check attendance
    try:
        attendance = float(input("Enter your attendance percentage: "))
        if attendance >= 75:
            print("You are allowed to take the exam.")
        else:
            print("You are NOT allowed to take the exam.")
    except ValueError:
        print("Invalid attendance input! Please enter a number.")
else:
    print("Invalid input! Please enter 'Y' or 'N'.")