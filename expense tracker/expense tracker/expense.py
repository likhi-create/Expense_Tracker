def add_expense():
    amount = float(input("Enter expense amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")

    data = f"{amount}|{category}|{description}\n"

    return data


def display_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n----- All Expenses -----")

    for expense in expenses:
        amount, category, description = expense.strip().split("|")

        print("Amount      :", amount)
        print("Category    :", category)
        print("Description :", description)
        print("------------------------")