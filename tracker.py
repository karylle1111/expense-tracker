# Project: Expense Tracker | Installment 3: The Tracker Does Math
# Author: Maboloc, Karylle B.
# This program takes user input, calculates a subtotal, tax, and budget remaining.

print("=" * 40)
print("            EXPENSE TRACKER        ")
print("        Know where your money goes.")
print("=" * 40)

print()
print("MAIN MENU")
print("[1] Add an expense            (coming soon)")
print("[2] View all expenses         (coming soon)")
print("[3] Show total spent          (coming soon)")
print("[4] Exit                      (coming soon)")

print()
name = input("What's your name? ")
print("Welcome,", name + "! Let's log two expenses.")
subtotal = 0

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2
average = subtotal / 2

tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
tax = subtotal * (tax_percent / 100)
total = subtotal + tax
over_budget = total > budget
left = budget - total

print()
print("-" * 40)
print("SUMMARY")
print("  - ", item1, ":\t$", amount1, sep="")
print("  - ", item2, ":\t$", amount2, sep="")
print("Subtotal:\t$", subtotal, sep="")
print("Average:\t$", average, sep="")
print("Tax (", tax_percent, "%):\t$", tax, sep="")
print("Grand total:\t$", total, sep="")
print("Over budget?\t", over_budget, sep="")
print("Left in budget:\t$", left, sep="")
print("-" * 40)
print("Made by: Karylle Maboloc  |  Installment 3")