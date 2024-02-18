import csv
import os
import sqlite3

DATABASE_TYPE = None

# Check if SQLite database exists
if os.path.exists('expenses.db'):
    DATABASE_TYPE = 'sqlite'
else:
    DATABASE_TYPE = 'csv'

# Function to initialize the database
def initialize_database():
    if DATABASE_TYPE == 'sqlite':
        conn = sqlite3.connect('expenses.db')
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            date TEXT,
            category TEXT,
            amount REAL
        )
        ''')

        conn.commit()
        conn.close()

# Function to load expenses from CSV file
def load_expenses(filename):
    expenses = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)
    return expenses

# Function to save expenses to CSV file
def save_expenses(filename, expenses):
    with open(filename, 'w', newline='') as file:
        fieldnames = ['date', 'category', 'amount']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)

# Function to add an expense
def add_expense(date, category, amount):
    if DATABASE_TYPE == 'sqlite':
        conn = sqlite3.connect('expenses.db')
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO expenses (date, category, amount) VALUES (?, ?, ?)
        ''', (date, category, amount))

        conn.commit()
        conn.close()
        print("Expense added successfully.")
    else:
        expenses = load_expenses('expenses.csv')
        expenses.append({'date': date, 'category': category, 'amount': amount})
        save_expenses('expenses.csv', expenses)
        print("Expense added successfully.")

# Function to retrieve all expenses
def get_all_expenses():
    if DATABASE_TYPE == 'sqlite':
        conn = sqlite3.connect('expenses.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM expenses')
        expenses = cursor.fetchall()

        conn.close()
        return expenses
    else:
        expenses = load_expenses('expenses.csv')
        return expenses

# Main function
def main():
    initialize_database()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))  # Assuming amount is a float
            add_expense(date, category, amount)
        elif choice == '2':
            expenses = get_all_expenses()
            if not expenses:
                print("No expenses recorded.")
            else:
                print("ID\tDate\t\tCategory\tAmount")
                for expense in expenses:
                    print(f"{expense[0]}\t{expense[1]}\t{expense[2]}\t\t{expense[3]}")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
