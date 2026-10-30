# Project: Expense Tracker | Installment 5: The Menu Comes Alive
# Author: Maboloc, Karylle B.
# This program uses a while loop to make the menu functional.

print("=" * 40)
print("            EXPENSE TRACKER        ")
print("        Know where your money goes.")
print("=" * 40)
print()

name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

print("Welcome, " + name + "!")
subtotal = 0
count = 0

while True:
    print()
    print("MAIN MENU")
    print("[1] Add an expense")
    print("[2] View all expenses         (coming soon)")
    print("[3] Show total spent")
    print("[4] Exit")
    
    choice = input("Choose 1-4: ")
    
    if choice == "1":
        amount = float(input("Amount? "))
        subtotal += amount
        count += 1
        
        if amount > 200:
            print("Huge expense - are you sure?")
        elif amount > 100:
            print("Big expense.")
        elif amount > 50:
            print("Moderate expense.")
        else:
            print("Small expense.")
            
    elif choice == "2":
        print("Coming soon: the tracker can't remember each item yet.")
        
    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax
        over_budget = total > budget
        
        print("Expenses:\t", count, sep="")
        print("Subtotal:\t$", subtotal, sep="")
        print("Tax (", tax_percent, "%):\t$", tax, sep="")
        print("Grand total:\t$", total, sep="")
        
        if over_budget:
            print("Over budget by $", total - budget, "!", sep="")
        elif total > (budget * 0.9):
            print("Careful: only $", budget - total, " left.", sep="")
        else:
            print("Within budget. $", budget - total, " left.", sep="")
            
    elif choice == "4":
        print("Goodbye, " + name + "!")
        print("-" * 40)
        print("Made by: Karylle Maboloc  |  Installment 5")
        print("=" * 40)
        break
        
    else:
        print("Please choose 1, 2, 3 or 4.")