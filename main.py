from datetime import datetime
from Expense import CategorizedExpense
from ExpenseTracker import ExpenseTracker
from categories import ExpenseCategory


# Example usage
tracker = ExpenseTracker()


def get_enum_item_by_index(enum_class, index):
    if 0 <= index < len(enum_class):
        return list(enum_class)[index]
    raise IndexError("Enum index out of range")


# console app initial display
while True:
    print("\nEXPENSE TRACKING!")
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
        for index, category in enumerate(ExpenseCategory):
            print(f"{index + 1}:{category.value} ")

        # select category number from listed categories above
        category_input = int(input("Enter the expense category: "))
        if category_input > 0:
            category_input -= 1

        category = None
        teCateory = get_enum_item_by_index(ExpenseCategory, category_input)
        print(teCateory.name)

        for enum_category in ExpenseCategory:
            if enum_category.value == teCateory.value:
                category = enum_category
                break
        if category is None:
            print("Invalid category. Please select again")
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
    # list of choices for viewing expenses
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
