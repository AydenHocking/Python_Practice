#Imported data from other files
import data
from cashier import Cashier
from sandwich_maker import SandwichMaker

# Make an instance of other classes here
resources = data.resources                                                                           ##resources instance
recipes = data.recipes                                                                               ##recipes instance
sandwich_maker_instance = SandwichMaker(data.resources)                                              ##SandwichMaker instance
cashier_instance = Cashier()                                                                         ##Cashier instance




def main():
    while True:
        selection = input("What would you like? (small/medium/large/off/report/add): ").lower()     ##Input selections formatted.
        if selection in recipes:                                                                    ##Checks if the input is small/medium/large.
            sandwich = recipes[selection]                                                           ##selects sandwich with selection name.
            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):                    ##Runs check_resources for true value.
                payment = cashier_instance.process_coins()                                          ##Assigns payment to coins from running process_coins.
                if cashier_instance.transaction_result(payment, sandwich["cost"]):                  ##Runs transaction_result for true value.
                    sandwich_maker_instance.make_sandwich(selection, sandwich["ingredients"])       ##Runs make_sandwich.
        elif selection == "report":                                                                 ##Checks if input is "report".
            for item, amount in resources.items():                                                  ##Iterates through the resource items.
                if item == "bread" or item == "ham":                                                ##Checks if item is "bread" or "ham".
                    print(str(item) + ": " + str(amount) + " slices")                               ##Prints slices.
                else:
                    print(str(item) + ": " + str(amount) + " ounces")                               ##Prints ounces(cheese).
        elif selection == "off":                                                                    ##Checks if input is "off".
            print("Turning off the sandwich machine.")
            break                                                                                   ##End program with code 0.
        elif selection == "add":                                                                    ##Checks if input is "add". Added to maintain steady resource amount without program re-execution.
            add_bread = int(input("How many bread slices would you like to add? "))                 ##Input bread to add.
            add_ham = int(input("How many ham slices would you like to add? "))                     ##Input ham to add.
            add_cheese = int(input("How many cheese ounces would you like to add? "))               ##Input cheese to add.
            sandwich_maker_instance.add_resources({"bread": add_bread, "ham": add_ham, "cheese": add_cheese})
        else:
            print("Sorry, that's not a valid option.")                                              ##Error check.

if __name__=="__main__":
    main()