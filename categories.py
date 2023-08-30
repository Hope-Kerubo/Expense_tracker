from enum import Enum


# list of categories that a user can select from
class ExpenseCategory(Enum):
    FOOD = "Food"
    RENT = "Rent"
    HEALTHCARE = "Healthcare"
    PERSONALCARE = "Personal Care"
    TRANSPORTATION = "Transportation"
    ENTERTAINMENT = "Entertainment"
    SAVINGS = "Savings"
    UTILITIES = "Utilities"
    OTHER = "Other"
