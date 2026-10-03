# Project: Expense Tracker | Installment 2: Talking to the User
# Author: Maboloc, Karylle B.
# This program takes user input for expenses, calculates, and displays a summary.

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

item1 = input("First expense? ")
amount1 = float(input("Amount? "))

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print()
print("-" * 40)
print("SUMMARY")
print("  -", item1 + ":     $", amount1)
print("  -", item2 + ":      $", amount2)s
print("Total spent:    $", total)
print("Average:        $", average)

print("-" * 40)
print("Made by: Karylle Maboloc  |  Installment 2")