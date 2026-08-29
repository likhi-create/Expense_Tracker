FILE_NAME = "expenses.txt"


def save_expense(data):
    with open(FILE_NAME, "a") as file:
        file.write(data)


def read_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return file.readlines()

    except FileNotFoundError:
        return []


def delete_expenses():
    with open(FILE_NAME, "w") as file:
        file.write("")