from datetime import datetime
from categories import ExpenseCategory


class Expense:
    def __init__(self, amount, description, date):
        self.amount = amount
        self.description = description
        self.date = date

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d')} - ${self.amount:.2f} - {self.description}"

class CategorizedExpense(Expense):
    def __init__(self, amount, description, date, category):
        super().__init__(amount, description, date)
        self.category = category

    def __str__(self):
        return super().__str__() + f" ({self.category.value})"

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            removed_expense = self.expenses.pop(index)
            print(f"Removed expense: {removed_expense}")
        else:
            print("Invalid index.")

    def list_expenses(self):
        if not self.expenses:
            print("No expenses to display.")
        else:
            print("Expenses:")
            for index, expense in enumerate(self.expenses):
                print(f"{index}: {expense}")

    def list_expenses_by_category(self, category):
        matching_expenses = [expense for expense in self.expenses if expense.category == category]
        if not matching_expenses:
            print(f"No expenses in the {category.value} category.")
        else:
            print(f"Expenses in the {category.value} category:")
            for index, expense in enumerate(matching_expenses):
                print(f"{index}: {expense}")

    def list_expenses_by_date(self, date):
        matching_expenses = [expense for expense in self.expenses if expense.date == date]
        if not matching_expenses:
            print(f"No expenses on {date.strftime('%Y-%m-%d')}.")
        else:
            print(f"Expenses on {date.strftime('%Y-%m-%d')}:")
            for index, expense in enumerate(matching_expenses):
                print(f"{index}: {expense}")

# Example usage
tracker = ExpenseTracker()

while True:
    print("\nOptions:")
    print("1. Add Expense")
    print("2. Remove Expense")
    print("3. List Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter the expense amount: "))

        # Display available categories
        print("Available Categories:")
        for index,category in enumerate(ExpenseCategory):
            print(f"{index+1}:{category.value} ")

        category_input = input("Enter the expense category: ")
        category = None
        for enum_category in ExpenseCategory:
            if enum_category.value == category_input:
                category = enum_category
                break
        if category is None:
            print("Invalid category.")
            continue
        description = input("Enter a description: ")

        date_str = input("Enter the date (YYYY-MM-DD): ")
        date = datetime.strptime(date_str, "%Y-%m-%d")
        expense = CategorizedExpense(amount, description, date, category)
        tracker.add_expense(expense)
        print("Expense added successfully.")
    elif choice == "2":
        index = int(input("Enter the index of the expense to remove: "))
        tracker.remove_expense(index)
    elif choice == "3":
        print("a. List all Expenses")
        print("b. List Expenses by Category")
        print("c. List Expenses by Date")
        print("d. Exit")
        choice = input("Enter your choice: ")
        if choice == "a":
           tracker.list_expenses()
        elif choice == "b":
            category_input = input("Enter the category to filter by: ")
            category = None
            for enum_category in ExpenseCategory:
                if enum_category.value == category_input:
                    category = enum_category
                    break
            if category is None:
                print("Invalid category.")
            else:
                tracker.list_expenses_by_category(category)
        elif choice == "c":
            date_str = input("Enter the date (YYYY-MM-DD) to filter by: ")
            # error handling
            try:
                date = datetime.strptime(date_str, "%Y-%m-%d")
                tracker.list_expenses_by_date(date)
            except ValueError:
                print("Invalid date format.")

    elif choice == "4":
        print("Exiting.")
        break
    else:
        print("Invalid choice. Please choose again.")