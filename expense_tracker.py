from expense import Expense


def main():

    expense_file = "expenses.csv"
    budget = 2000

    # Get user input fro expense
    expense = get_user_expense()

    # Write this expense to a file
    save_expense_to_file(expense, expense_file)

    # Read the file and summerize expense
    summerize_expense(expense_file, budget)


def get_user_expense():
    print(f"🎯Getting the user expense")

    expense_name = input("Enter expense name: ")

    expense_amount = float(input("Enter your expense amount: "))

    expense_categories = [
        "🍔 Food",
        "🏠 Home",
        "💼 Work",
        "🎊 Fun",
        "✨ Other",
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f" {i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_value = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_value in range(len(expense_categories)):
            selected_category = expense_categories[selected_value]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount
            )
            return new_expense
        else:
            print("Invalid category, please try again!")


def save_expense_to_file(expense: Expense, expense_file):
    print(f"🎯 Saving the user expense: {expense} to {expense_file}")
    with open(expense_file, "a", encoding="utf-8") as f:
        f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")


def summerize_expense(expense_file, budget):
    print(f"🎯 Summarizing the user expenses")
    expenses = []  # List to store Expense objects
    total_expense = 0
    amount_by_category = {}  # Dictionary to store totals by category

    try:
        with open(expense_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if not lines:
                print("No expenses found.")
                return

            print("Here is the summary of your expenses:")
            for line in lines:
                line = line.strip()
                if not line:
                    continue

                # Parse the expense details
                expense_name, expense_amount, expense_category = line.split(", ")
                expense_amount = float(expense_amount)
                total_expense += expense_amount

                # Append to expenses list
                expenses.append(
                    Expense(
                        name=expense_name,
                        amount=expense_amount,
                        category=expense_category,
                    )
                )

                # Print individual expense
                print(f"{expense_name} ({expense_category}): ${expense_amount:.2f}")

                # Add to category totals
                if expense_category in amount_by_category:
                    amount_by_category[expense_category] += expense_amount
                else:
                    amount_by_category[expense_category] = expense_amount

            # Print the total summary
            print(f"\nTotal Expenses: ${total_expense:.2f}")
            print("\nExpenses by Category:")
            for category, total in amount_by_category.items():
                print(f"  {category}: ${total:.2f}")

            # Calculate remaining budget
            remaining_budget = budget - total_expense
            print(f"\nYour Remaining Budget: ${remaining_budget:.2f}")

            # Optional: Save the remaining budget to a file for persistence
            # If you want to save the remaining budget back to a file:
            with open("budget.txt", "w") as budget_file:
                budget_file.write(str(remaining_budget))

    except FileNotFoundError:
        print(f"⚠️ File '{expense_file}' not found. No expenses to summarize.")
    except ValueError as e:
        print(f"⚠️ Error while reading the file: {e}")


if __name__ == "__main__":
    main()
