import csv
import os
from datetime import date
from datetime import datetime

def crtexp_csv():
    header = ['Date', 'Category', 'Amount']
    with open('expenses.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

def addexp_csv(date, category, amount):
    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

def vuexp_csv():
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

if not os.path.exists('expenses.csv'):
    crtexp_csv()
x=int(input("TOTAL ENTRY"))
while x>0:
    dt1=int(input("ENTER THE CHOICE:-\n"))
    if dt1==0:
        user_date_input = input("Enter expense date (YYYY-MM-DD): ")
        try:
            formatted_date = datetime.strptime(user_date_input, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            exit()
    else:
        today = date.today()
        formatted_date = today.strftime("%Y-%m-%d")
    category = input("Enter expense category: ")
    amount = input("Enter expense amount: ")
    addexp_csv(formatted_date, category, amount)
    x-=1
print("\nAll Expenses:")
vuexp_csv()
