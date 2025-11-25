# Ayden Hocking 1/28/2025
from BankAccount import BankAccount
from SavingsWithInterest import SavingsAccount
from CheckingWithTransferLimitation import CheckingAccount
def main():
    savingsCustomer1 = SavingsAccount("John Doe", 1000, 200, "123456789", "987654321")
    savingsCustomer1.print_customer_information()
    savingsCustomer1.deposit(100)
    savingsCustomer1.withdraw(1000)
    
    print("\n")

    savingsCustomer2 = SavingsAccount("Sam Ross", 3000, 400, "888888888", "222222222")
    savingsCustomer2.print_customer_information()
    savingsCustomer2.deposit(400)
    savingsCustomer2.withdraw(1000)
    
    print("\n")
    
    checkingCustomer1= CheckingAccount("Jane Smith", 500, 100, "987654321", "123456789")
    checkingCustomer1.print_customer_information()
    checkingCustomer1.withdraw(2001)
    checkingCustomer1.deposit(200)

    print("\n")

    checkingCustomer2= CheckingAccount("Tim Brown", 1000, 200, "999999999", "111111111")
    checkingCustomer2.print_customer_information()
    checkingCustomer2.withdraw(50)
    checkingCustomer2.deposit(100)

if __name__=="__main__":
    main()


