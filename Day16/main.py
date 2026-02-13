from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create all the variables
coffee_menu = Menu()
money_storage = MoneyMachine()
coffee_machine = CoffeeMaker()


is_on = True
while is_on:
    choice = input(f"What would you like? ({coffee_menu.get_items()}): ").lower()

    if choice == "report":
        coffee_machine.report()
        money_storage.report()
    elif choice == "off":
        print("Machine shutting down...")
        is_on = False
    else:
        drink = coffee_menu.find_drink(choice)
        if drink is not None:
            if coffee_machine.is_resource_sufficient(drink):
                if money_storage.make_payment(drink.cost):
                    coffee_machine.make_coffee(drink)

