# Expense-app
 # Main function that serves as the entry point of the program.
def main():
    print(f"Running Expense Tracker!")  # Displaying program start message.
    expense_file_path = "expenses.csv"  # File path to store expenses.

# Gather user input for a new expense.
    expense = get_user_expense()
# Save the new expense to a file.
    save_expense_to_file(expense, expense_file_path)
# Read and summarize all expenses from the file.
    summarize_expenses(expense_file_path)

# Function to get expense details from the user.
def get_user_expense():
    print(f"Getting user Expense")
    expense_name = input("Enter Expense Name: ")  # Prompting the user


    expense_amount = float(input("Enter Expense Amount: "))  # Prompting the user for the expense amount and converting it to a float.

# Predefined list of expense categories to choose from.
    expense_categories = [
        "Food", 
        "Work", 
        "Home", 
        "Fun", 
        "Misc"
    ]

# Loop until the user selects a valid category.
    while True:
        print("Select a category for the expense:")
# Displaying available categories with their corresponding indices.
        for i, category_name in enumerate(expense_categories):
            print(f" {i + 1}. {category_name}")
        
# Prompting the user to select a category by its number.
        val_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {val_range}: ")) - 1
        
# Check if the selected index is valid.
        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]  # Assigning the selected category.
# Creating an instance of the Expense object with the provided details.
            new_expense = Expense(
                name=expense_name, amount=expense_amount, category=selected_category
            )
            return new_expense  # Returning the newly created Expense object.
        else:
            print(f"Invalid category selected. Try again.")  # Invalid input message.

# Function to save an expense to the file.
def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"Saving Expense to file: {expense} to {expense_file_path}")
# Open the file in append mode to add new expense data.
    with open(expense_file_path, "a") as f:
        # Write the expense details as a comma-separated line.
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

# Function to read expenses from the file and display a summary.
def summarize_expenses(expense_file_path, budget=800):
    print(f"Summarizing Expenses")
    expenses = []  # List to store all expense objects.
    
# Open the file in read mode to fetch expense data.
    with open(expense_file_path, "r") as f:
        lines = f.readlines()  # Read all lines from the file.
        for line in lines:
            stripped_line = line.strip()  # Remove leading/trailing whitespace.
# Split the line into its components: name, amount, and category.
            expense_name, expense_amount, expense_category = stripped_line.split(",")
# Create an Expense object from the line data.
            line_expense = Expense(
                name=expense_name, 
                amount=float(expense_amount), 
                category=expense_category
            )
            expenses.append(line_expense)  # Add the Expense object to the list.

# Dictionary to store the total amount spent by category.
    amount_by_category = {}
    for expense in expenses:
        key = expense.category  # Use the category as the dictionary key.
# Add the expense amount to the category total.
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

# Displaying expenses grouped by category.
    print("Expenses by Category📈:")
    for key, amount in amount_by_category.items():
        print(f" {key}: ${amount:.2f}")
 # Calculate and display the total amount spent.
    total_spent = sum(expense.amount for expense in expenses)
    print(f"💸You've Spent: ${total_spent:.2f} This Semester")

# Calculate remaining budget.
    remaining_budget = budget - total_spent
    if remaining_budget < 0:
# Warn if the user has exceeded their budget.
        print(red(f"WARNING⚠️: You've exceeded your budget by ${abs(remaining_budget):.2f} call mommy for help"))
    elif remaining_budget < budget // 2:
# Warn if the remaining budget is less than half.
        print(yellow(f"Budget Remaining⚠️: ${remaining_budget:.2f} Until Break"))
    else:
# Display the remaining budget.
        print(f"Budget Remaining: ${remaining_budget:.2f} Until Break")
    
# Calculate the number of days remaining until Spring Break.
    today = datetime.date.today()
    spring_break = datetime.date(today.year, 2, 28)  # Set Spring Break date as February 28.
    if today > spring_break:
        spring_break = datetime.date(today.year + 1, 2, 28)  # Adjust for next year's Spring Break if today is past February 28.
    days_until_break = (spring_break - today).days  # Calculate remaining days.
    
# Calculate the daily budget until Spring Break.
    daily_budget = remaining_budget / days_until_break
    if daily_budget < 10:
# Warn if the daily budget is very low.
        print(red(f"Daily Budget until Spring Break: 💵 ${daily_budget:.2f}"))
    else:
# Display the daily budget.
        print(green(f"Daily Budget until Spring Break: 💵 ${daily_budget:.2f}"))

# Helper function to print text in red (for warnings).
def red(text):
    return f"\033[91m{text}\033[0m"

# Helper function to print text in yellow (for caution).
def yellow(text):
    return f"\033[93m{text}\033[0m"

# Helper function to print text in green (for positive messages).
def green(text):
    return f"\033[92m{text}\033[0m"

# Run the main function when the script is executed.
if __name__ == "__main__":
    main()