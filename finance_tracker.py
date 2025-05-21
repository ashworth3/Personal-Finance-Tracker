# Personal Finance Tracker

# Allows users to add expenses with descriptions and categories
def add_expense(data):
    try:
        description = input("Enter the expense description: ").strip()
        if not description:
            raise ValueError("Description cannot be empty.")
        
        category = input("Enter the expense category: ").strip()
        if not category:
            raise ValueError("Category cannot be empty.")
        
        amount_input = input("Enter the expense amount: $").strip()
        amount = float(amount_input)
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        if category not in data:
            data[category] = []
        
        data[category].append({"description": description, "amount": amount})
        print(f"Expense added: {description} in category {category} for ${amount:.2f}")
    except ValueError as ve:
        print(f"Invalid Input: {ve}")
    except Exception as e:
        print(f"An unexpected error has occured: {e}")

# Allows users to view all expenses categorized by type
def view_expenses(data):
    if not data:
        print("No expenses recorded.")
        return
    
    print("\nExpenses:")
    for category, expenses in data.items():
        print(f"\nCategory: {category}")
        for expense in expenses:
            print(f"  - {expense['description']}: ${expense['amount']:.2f}")
    print("\n")

# Provides a summary of total expenses by category
def view_summary(data):
    if not data:
        print("No expenses recorded.")
        return
        
    print("\nSummary:")
    for category, expenses in data.items():
        total = sum(expense["amount"] for expense in expenses)
        print(f"{category}: ${total:.2f}")

# Main function to run program
def main():
    print("Welcome to the Personal Finance Tracker!")
    data = {}

    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            add_expense(data)
        elif choice == '2':
            view_expenses(data)
        elif choice == '3':
            view_summary(data)
        elif choice == '4':
            print("Exiting, Goodbye!")
            break
        else:
            print("Invalid choice. Please choose (1-4).")

if __name__ == "__main__":
    main()