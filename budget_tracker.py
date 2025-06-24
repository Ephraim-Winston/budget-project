import csv
from datetime import datetime
#why is the import syntax different for these two
#Initialize transactions list

date = input("Date of Transaction: ")
description = float(input("Transaction Description: "))
amount = input("Transaction Amount: ")


class Transaction:
    #The __init__ method initializes the attributes (variables) of an object when a class instance is created.
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount= float(amount)

    def display(self):
        #Display a formatted string of the transaction
        #What is difference between formatted and unformatted
        return f"Date:{self.date}, Description: {self.description}, Amount: {self.amount}"



class Budget:
    def __init__(self):
        #initialize with an empty list of transactions
        self.transactions=[] 

    def add_transaction(self, date, description,amount):
        #Transaction(self, date, description, amount) This is calling an instance of the Transaction class inside of the budget class method.
        new_transaction = Transaction(date, description, amount)
        self.transactions.append(new_transaction)

    def remove_transaction(self, index):
        if 0<= index < len(self.transactions):
            del self.transactions[index]

    def calculate_balance(self):
        return sum([transaction.amount for transaction in self.transactions])
    
    def display_transactions(self):
        for transaction in self.transactions:
            print(transaction.display())
    def save_to_csv(self, filename):
        with open(filename, 'w', newline= '') as file:
            writer = csv.writer(file)
            writer.writerow(['Date','Description','Amount'])
            for transaction in self.transactions:
                writer.writerow([transaction.date,transaction.description, transaction.amount])

    def load_from_csv(self, filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    date = row[0]
                    description = row[1]
                    amount = float(row[2])
                    self.add_transaction(date,description,amount)
        except FileNotFoundError:
            print(f"Error: {filename} not found.")

# Example usage
'''''
my_budget = Budget()
my_budget.add_transaction("2025-01-14", "Grocery shopping", -50.0)
my_budget.add_transaction("2025-01-15", "Salary", 1000.0)

my_budget.display_transactions()  # Show all transactions
print(f"Balance: {my_budget.calculate_balance()}")  # Show current balance

# Save and load transactions
my_budget.save_to_csv("transactions.csv")
my_budget.load_from_csv("transactions.csv")
'''