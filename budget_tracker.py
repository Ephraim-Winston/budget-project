import csv 
from datetime import datetime
#why is the import syntax different for these two
#Initialize transactions list

FILENAME = "transactions.csv"



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
    
    def input_transaction_loop(self, filename = FILENAME):
        while True:
            #i remember this function was changed and was "broken up" like we discussed yesterday. I still don't get why.
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            self.add_transaction(date, description, amount)
            self.save_to_csv(filename)

            if input("Add another? (y/n): ").lower() != 'y':
                break

    def remove_transaction(self, index):
        #function takes in an index as it's argument
        if 0<= index < len(self.transactions):
            #ensured that the index is within the range of the self.transaction array
            del self.transactions[index]
            #after taking in a number/index as an argument delete the transaction at the provided index inside of self.transactions

    def calculate_balance(self):
        #function does not take in any arguments...interesting. other than self which "isn't a parameter".
        return sum([transaction.amount for transaction in self.transactions])
        #Above is a list commprehension. Inside of an array [] we have a for loop iterating through self.transactions, which is an array of transaction objects created by Transaction.
        #Iterating through each transaction the loop will extract transaction.amount accesing the amount values and placing each value into our array return sum([amount, amount,amount ])
    
    def display_transactions(self):
        for transaction in self.transactions:
            print(transaction.display())
    def save_to_csv(self, filename):
        #takes in a filename as a parameter...maybe i should restrict rile types here.
        with open(filename, 'w', newline= '') as file:
            #takes in file name as a write file and stores it in the "file" variable i think newline='' makes sure to not have any extra blank lines in between files
            writer = csv.writer(file)
            #i think attatching a writer object to file
            writer.writerow(['Date','Description','Amount'])
            #so that here we can access the writer object and use it's writerow method to create a header for our columns of date description and amount 
            for transaction in self.transactions:
                #loop through transactions in our budgets objects self.transactions = [] attribute and for each transactions write in a row the values of the transactions date, description, and amount 
                writer.writerow([transaction.date,transaction.description, transaction.amount])
    #FUNCTIONALITY TO ADD: this funcntion needs to check if data exists in csv how to check if csv has data?
    def load_from_csv(self, filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                #The built-in next() function in Python is used to retrieve the next item from an iterator. 
                for row in reader:
                    date = row[0]
                    description = row[1]
                    amount = float(row[2])
                    self.add_transaction(date,description,amount)
        except FileNotFoundError:
            print(f"Error: {filename} not found.")

# Example usage


if __name__ == "__main__":
    my_budget = Budget()
    my_budget.load_from_csv(FILENAME)
    my_budget.input_transaction_loop()
    my_budget.display_transactions()


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