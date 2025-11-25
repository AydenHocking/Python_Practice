class BankAccount:
    bankName = "PythonBank"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self.account_number = account_number
        self.routing_number = routing_number

    def deposit(self, amount):
        print("-------------------------------------------")
        print("Depositing amount...", amount)
        if amount > 0:
            self.current_balance += amount
            print("Deposit Successful")
            print("Current Balance: ", self.current_balance)
        else:
            print("Deposit Failed, enter a positive number")
            print("Current Balance: ", self.current_balance)

    def withdraw(self, amount):
        print("-------------------------------------------")
        print("Withdrawing amount...", amount)
        if amount > 0:
            if (self.current_balance - amount) > self.minimum_balance:
                self.current_balance -= amount
                print("Withdrawal Successful")
                print("Current Balance: ", self.current_balance)
            else:
                print("Withdrawal Failed, not enough funds")
                print("Current Balance: ", self.current_balance)
        else:
            print("Withdrawal Failed, enter a positive number")
            print("Current Balance: ", self.current_balance)

    def print_customer_information(self):
        print("-------------------------------------------")
        print(self.bankName + " Customer:")
        print("-------------------------")
        print("Name: " + self.customer_name + "\nAccount Number: " + str(
            self.account_number) + "\nRouting Number: " + str(self.routing_number) + "\nCurrent Balance: " + str(
            self.current_balance) + "\nMinimum Balance: " + str(self.minimum_balance))
        print("-------------------------")
