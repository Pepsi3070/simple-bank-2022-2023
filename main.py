1.uzd
ruby
Copy code
class Customer:
    def init(self, name, balance):
        self.name = name
        self.balance = balance

    def calculate_percentages(self, years):
        interest_rate = 0.005
        total_interest = self.balance * interest_rate * years
        return total_interest

2.uzd

from datetime import datetime

class Human:
    def init(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email
        self.datetime_created = datetime.now()

class Customer(Human):
    def init(self, name, surname, email, balance):
        super().init(name, surname, email)
        self.balance = balance

    def calculate_percentages(self):
        percentages = self.balance * 0.005
        return percentages

        3.uzd

        import csv

def save_customers_to_csv(customers, file_path):
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        # Raksta galvenes
        writer.writerow(['name', 'surname', 'email', 'datetime_created'])
        
        # Raksta katru rindiņu
        for customer in customers:
            writer.writerow([
                customer.name,
                customer.surname,
                customer.email,
                customer.datetime_created.strftime('%Y-%m-%d %H:%M:%S')
            ])

4.uzd

import csv

def display_customer_csv():
    with open('customers.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

5.uzd

import csv
from datetime import datetime

class Human:
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email
        self.datetime_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class Customer(Human):
    def __init__(self, name, surname, email, deposit):
        super().__init__(name, surname, email)
        self.deposit = deposit

    def calculate_percentages(self):
        return self.deposit * 0.005

    def modify_customer(self):
        print(f"Current name: {self.name}")
        new_name = input("Enter new name: ")
        print(f"Current surname: {self.surname}")
        new_surname = input("Enter new surname: ")
        print(f"Current email: {self.email}")
        new_email = input("Enter new email: ")
        self.name = new_name
        self.surname = new_surname
        self.email = new_email
        print("Customer data has been modified.")

def create_customer_csv(customers):
    with open("customers.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Surname", "Email", "Deposit", "Created", "Percentages"])
        for customer in customers:
            percentages = customer.calculate_percentages()
            writer.writerow([customer.name, customer.surname, customer.email, customer.deposit, customer.datetime_created, percentages])

def display_customer_csv():
    with open("customers.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

    choice = input("Which customer would you like to modify? Enter the row number: ")
    customers = []
    with open("customers.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            customer = Customer(row["Name"], row["Surname"], row["Email"], int(row["Deposit"]))
            customer.datetime_created = row["Created"]
            customers.append(customer)

    chosen_customer = customers[int(choice) - 1]
    chosen_customer.modify_customer()

    create_customer_csv(customers)

    print("CSV file has been updated.")

6.uzd

import random
import datetime

class Account:
    def __init__(self, number, owner, balance, creation_date):
        self.number = number
        self.owner = owner
        self.balance = balance
        self.creation_date = creation_date
        
        if self.is_april_fools():
            self.generate_prize()
        
    def is_april_fools(self):
        return self.creation_date.month == 4 and self.creation_date.day == 1
        
    def generate_prize(self):
        prize = random.randint(1, 100)
        self.balance += prize
        print(f"Congratulations! You have won {prize}$!")
