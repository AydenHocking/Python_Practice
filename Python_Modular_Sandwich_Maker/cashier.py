class Cashier:
    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Insert coins:")                                                                      ##Collection of inputs for coins.
        dollars = int(input("How many dollars?: "))
        half_dollars = int(input("How many half dollars?: "))
        quarters = int(input("How many quarters?: "))
        nickles = int(input("How many nickles?: "))
        coins = round(float(dollars * 1 + half_dollars * 0.5 + quarters * 0.25 + nickles * 0.05),2) ##Adds all coin amounts * their worth. Then rounds to two digits to prevent error.
        return coins


    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if cost > coins:                                                                            ##Checks if the user paid enough for sandwich cost.
            print("Sorry that's not enough money. Money refunded.")
            return False
        else:
            change = coins - cost                                                                   ##Determine change.
            print("Here is $%.2f in change." % change)                                              ##Formats change to 2 decimal places.
            return True
