import csv
from datetime import datetime

#Initialize transactions list
transactions = []

#function to add a transaction...should triggered by a button?
def add_transactions(date, t_type, amount, category):
    transactions.append({
        "date": date,
        "type":t_type,
        "amount": amount,
        "category": category 
    })

def view_transactions():
    for i, t in enumerate(transactions):
        print(f"{i+1}. Date: {t['date']},Type: {t['type']},Amount: {t['amount']} Category:{t['category']}")
    #why comma