from BankAccount import BankAccount


class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance,   account_number, routing_number):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transferLimit = 2000
    def deposit(self, amount):
        super().deposit(amount)
    
    def withdraw(self, amount):
        if amount > self.transferLimit:
            print("Transfer Limit Exceeded")
        else:
            super().withdraw(amount)
    
    def print_customer_information(self):
        super().print_customer_information()