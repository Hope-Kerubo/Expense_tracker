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
