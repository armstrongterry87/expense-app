import sys
import datetime
from typing import List
from expense import Expense

if sys.version_info < (3, 7):
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main():
    print(f"Running Expense Tracker!") 
    expense_file_path = "expenses.csv"
    
    #User input for expense
    expense = get_user_expense()
    #write expense to file
    save_expense_to_file(expense, expense_file_path)
    #read file and dis+play expenses
    summarize_expenses(expense_file_path)
    

def get_user_expense():
    print(f"Getting user Expense")
    expense_name = input("Enter Expense Name: ")
    expense_amount = float(input("Enter Expense Amount: "))
    
    expense_categories = [
        "Food", 
        "Work", 
        "Home", 
        "Fun", 
        "Misc"
    ]
    
    while True:
        print("Select a category for the expense:")
        for i, category_name in enumerate(expense_categories):
            print(f" {i + 1}. {category_name}")
        
        val_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {val_range}: ")) - 1
        
        
        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name = expense_name, amount = expense_amount, category = selected_category
                )
            return new_expense
        else:
            print(f"Invalid category selected. Try again.")
    

def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"Saving Expense to file: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

def summarize_expenses(expense_file_path, budget = 800):
    print(f"Summarizing Expenses")
    expenses = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip() 
            expense_name, expense_amount, expense_category = stripped_line.split(",")
            line_expense = Expense(
                name = expense_name, 
                amount = float(expense_amount), 
                category = expense_category
                )
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    
    print("Expenses by Category📈:")
    for key, amount in amount_by_category.items():
        print(f" {key}: ${amount:.2f}")
    
    total_spent = sum(expense.amount for expense in expenses)
    print(f"💸You've Spent: ${total_spent:.2f} This Semester")
    
    remaining_budget = budget - total_spent
    if remaining_budget < 0:
        print(red(f"WARNING⚠️: You've exceeded your budget by ${abs(remaining_budget):.2f} call mommy for help"))
    elif remaining_budget < budget//2:
        print(yellow(f"Budget Remaining⚠️: ${remaining_budget:.2f} Until Break"))
    else:
        print(f"Budget Remaining: ${remaining_budget:.2f} Until Break")
    
    today = datetime.date.today()
    spring_break = datetime.date(today.year, 2, 28)
    if today < spring_break:
        spring_break = datetime.date(today.year + 1, 2, 28)
        days_until_break = (spring_break - today).days
        daily_budget = remaining_budget / days_until_break
        if daily_budget < 10:
            print(red(f"Daily Budget until Spring Break: 💵 ${daily_budget:.2f}"))
        else: 
            print(green(f"Daily Budget until Spring Break: 💵 ${daily_budget:.2f}"))

def red(text):
    return f"\033[91m{text}\033[0m"

def yellow(text):
    return f"\033[93m{text}\033[0m"

def green(text):
    return f"\033[92m{text}\033[0m"

if __name__ == "__main__":
    main()


