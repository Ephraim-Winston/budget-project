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