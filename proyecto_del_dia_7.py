import os


class Person:
    def __init__(self, full_name):
        self.full_name = full_name


class Customer(Person):
    def __init__(self, full_name,  account_number, balance):
        super().__init__(full_name)
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return f"""
        Customer: {self.full_name}
        Account Number: {self.account_number}
        Balance: {self.balance}"""

    def deposit(self):
        amount = int(input("Enter the amount to deposit: "))
        return amount

    def withdraw(self, balance):
        amount = int(input("Enter the amount to withdraw: "))
        while amount > balance:
            print(f"The amount entered can't be greater than your balance: {balance}")
            amount = int(input("Enter the amount to withdraw: "))
        return amount


def create_customer():
    full_name = input("Ingrese nombre completo: ")
    the_customer = Customer( full_name, 1, 0)
    return the_customer


def show_menu(the_customer):
    print(f"Your balance is: {the_customer.balance}")
    print("""
    [1] - Deposit
    [2] - Whithdraw
    [3] - Exit""")
    customer_option = int(input("Your option: "))
    return customer_option


def start_program():
    the_customer = create_customer()
    print(the_customer)
    customer_option = 0
    while customer_option != 3:
        customer_option = show_menu(the_customer)
        if customer_option == 1:
            os.system('cls')
            amount = the_customer.deposit()
            the_customer.balance += amount
            print(f"You deposited {amount}")
            print(f"Your new balance is: {the_customer.balance}")
        elif customer_option == 2:
            os.system('cls')
            amount = the_customer.withdraw(the_customer.balance)
            the_customer.balance -= amount
            print(f"You drew {amount}")
            print(f"Your new balance is: {the_customer.balance}")
        elif customer_option == 3:
            break


start_program()
print("See you soon!")