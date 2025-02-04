class Expense:
    def __init__(self, name, category, amount):
        self.name = name
        self.category = category
        self.amount = amount

    def __str__(self):
        # Defines how the object is displayed when printed out
        return f"{self.name} ({self.category}): ${self.amount:.2f}"

    def __repr__(self):
        # Used for representing objects in lists, debug prints, etc.
        return (
            f"Expense(name={self.name}, category={self.category}, amount={self.amount})"
        )
