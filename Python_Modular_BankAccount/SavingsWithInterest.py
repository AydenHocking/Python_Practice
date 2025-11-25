from BankAccount import BankAccount


class SavingsAccount(BankAccount):

  def __init__(self, customer_name, current_balance, minimum_balance,
               account_number, routing_number):
    super().__init__(customer_name, current_balance, minimum_balance,
                     account_number, routing_number)
    self.interest_rate = 0.05

  def deposit(self, amount):
    super().deposit(amount)

  def withdraw(self, amount):
    super().withdraw(amount)

  def print_customer_information(self):
    super().print_customer_information()
    print("Interest Rate: " + str(self.interest_rate))
    
