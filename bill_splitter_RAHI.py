print("Welcome to the Bill Splitter App!")

repeat = "y"

while repeat.lower() == "y":
    bill = float(input("\nEnter total bill amount: "))
    if bill < 0:
        print("Error: Bill amount cannot be negative. Please try again.")
        continue 

    people = int(input("Enter number of people: "))
    tip_percentage = int(input("Enter tip percentage (0/5/10/15/20): "))
        
    tip_amount = (tip_percentage / 100) * bill
    final_bill = bill + tip_amount
    per_person = final_bill / people

    print(f"\nTip Amount: ₹{tip_amount:.2f}")
    print(f"Total Bill (with Tip): ₹{final_bill:.2f}")
    print(f"Each person should pay: ₹{per_person:.2f}")

    repeat = input("\nWould you like to calculate another bill? (y/n): ")

print("\nThank you for using the Bill Splitter App!")
