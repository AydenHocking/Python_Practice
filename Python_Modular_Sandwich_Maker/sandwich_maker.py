class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, amount in ingredients.items():                                                    ##Searches through the Items in Ingredients.
            if self.machine_resources[item] < amount:                                               ##Checks if there is enough of Item for making sandwich.
                print("Sorry, there is not enough " + str(item) + ".")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item, amount in order_ingredients.items():                                              ##Iterates through the items in the selected sandwich order.
            self.machine_resources[item] -= amount                                                  ##Remove Ingredients.
        print(str(sandwich_size) + " sandwich is ready. Bon appetit!")
    def add_resources(self, ingredients):
        for item, amount in ingredients.items():                                                    ##Iterates through the ingredients
            self.machine_resources[item] += amount