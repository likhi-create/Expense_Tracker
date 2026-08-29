import expense
import file_handler


def main():

    while True:

        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Delete All Expenses")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            data = expense.add_expense()
            file_handler.save_expense(data)

            print("Expense added successfully!")

        elif choice == "2":

            expenses = file_handler.read_expenses()
            expense.display_expenses(expenses)

        elif choice == "3":

            expenses = file_handler.read_expenses()

            total = 0

            for item in expenses:
                amount, category, description = item.strip().split("|")
                total += float(amount)

            print("Total Expenses: ₹", total)

        elif choice == "4":

            file_handler.delete_expenses()
            print("All expenses deleted.")

        elif choice == "5":

            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


main()