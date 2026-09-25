# ============================================
# Expense Tracker
# Description: A simple command-line expense
# tracker to log, categorize, and summarize
# personal expenses. Built as part of my
# Python learning journey.
# ============================================

# --- Data Storage ---
# We use a list to store each expense as a dictionary.
# A dictionary holds key-value pairs, like a row in a spreadsheet.
expenses = []

# --- Predefined Categories ---
# Keeping categories consistent makes analysis easier later.
CATEGORIES = ["Food", "Transport", "Housing", "Entertainment", "Health", "Other"]


# --- Functions ---

def add_expense(date, description, category, amount):
      """Add a new expense to the tracker."""
      # Validate that the category is one we recognize
      if category not in CATEGORIES:
                print(f"Invalid category. Please choose from: {', '.join(CATEGORIES)}")
                return

      # Validate that the amount is a positive number
      if amount <= 0:
                print("Amount must be greater than zero.")
                return

      # Create the expense as a dictionary and add it to our list
      expense = {
          "date": date,
          "description": description,
          "category": category,
          "amount": round(amount, 2)
      }
      expenses.append(expense)
      print(f"Added: {description} - ${amount:.2f} ({category})")


def view_all_expenses():
      """Display all logged expenses."""
      if not expenses:
                print("No expenses logged yet.")
                return

      print("\n--- All Expenses ---")
      for i, expense in enumerate(expenses, start=1):
                print(f"{i}. [{expense['date']}] {expense['description']} | "
                                    f"{expense['category']} | ${expense['amount']:.2f}")


def summary_by_category():
      """Show total spending grouped by category."""
      if not expenses:
                print("No expenses to summarize.")
                return

      # Use a dictionary to accumulate totals per category
      totals = {}
      for expense in expenses:
                cat = expense["category"]
                totals[cat] = totals.get(cat, 0) + expense["amount"]

      print("\n--- Spending by Category ---")
      for category, total in sorted(totals.items()):
                print(f"  {category}: ${total:.2f}")


def total_spent():
      """Return and display the total amount spent."""
      total = sum(expense["amount"] for expense in expenses)
      print(f"\nTotal Spent: ${total:.2f}")
      return total


# --- Main Program ---

def main():
      """Run the expense tracker menu loop."""
      print("Welcome to your Expense Tracker!")
      print(f"Categories available: {', '.join(CATEGORIES)}\n")

    while True:
              print("\nWhat would you like to do?")
              print("  1 - Add an expense")
              print("  2 - View all expenses")
              print("  3 - Summary by category")
              print("  4 - View total spent")
              print("  5 - Quit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
                      date = input("Date (YYYY-MM-DD): ").strip()
                      description = input("Description: ").strip()
                      print(f"Categories: {', '.join(CATEGORIES)}")
                      category = input("Category: ").strip().capitalize()
                      try:
                                        amount = float(input("Amount ($): ").strip())
except ValueError:
                print("Please enter a valid number for amount.")
                continue
            add_expense(date, description, category, amount)

elif choice == "2":
            view_all_expenses()

elif choice == "3":
            summary_by_category()

elif choice == "4":
            total_spent()

elif choice == "5":
            print("Goodbye! Keep tracking those expenses.")
            break

else:
            print("Invalid choice. Please enter a number between 1 and 5.")


# This ensures main() only runs when we execute this file directly,
# not when it's imported as a module elsewhere.
if __name__ == "__main__":
      main()
