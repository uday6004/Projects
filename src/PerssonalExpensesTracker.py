expenses = []


def add_expense():
    name = input("Enter expense name: ")

    try:
        amount = float(input("Enter expense amount: "))
    except ValueError:
        print("Please enter a valid amount.")
        return

    expenses.append([name, amount])
    print("Expense added successfully!")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    print("\n--- Expense List ---")

    for i in range(len(expenses)):
        print(i + 1, ".", expenses[i][0], "- Rs.", expenses[i][1])


def total_expense():
    total = 0

    for expense in expenses:
        total = total + expense[1]

    print("\nTotal Expense: Rs.", total)


def delete_expense():
    view_expenses()

    if len(expenses) == 0:
        return

    try:
        number = int(input("Enter expense number to delete: "))

        if 1 <= number <= len(expenses):
            removed = expenses.pop(number - 1)
            print("Deleted:", removed[0])
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expense()

        elif choice == "4":
            delete_expense()

        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram closed by user. Goodbye!")

