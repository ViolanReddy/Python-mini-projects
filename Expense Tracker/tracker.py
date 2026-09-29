expenses = []

print("Welcome to the Daily Expense Tracker!")
print()
print("\nMenu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expenses")
print("4. Clear all expenses")
print("5. Exit")

while True:
    choice = input("Enter your option(1-5): ")

    if choice == "5":
        print("Exiting Application...GoodBye!")
        break
    elif choice == "1":
        expense = float(input("Expense: "))
        expenses.append(expense)
        print("Expense added successfully!")
    elif choice == "2":
        for expense in expenses:
            print(expense)
    elif choice == "3":
        if not expenses:
            print("No expenses recorded!")
        else:
            total_expense = sum(expense)
            average_expense = total_expense / len(expenses)

            print(f"Total expense: {total_expense}")
            print(f"Average expense: {average_expense}")
    elif choice == "4":
        expenses.clear()
        print("All expenses cleared successfully!")
    else:
        print("Invalid input!")