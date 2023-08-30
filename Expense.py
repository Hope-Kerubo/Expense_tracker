class Expense:
    def __init__(self, amount: int, description: str, date):
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