from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

turn_off = False
menu = Menu()  # menu object
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
options = menu.get_items()

while not turn_off:
    choice = input(f"What would you like? ({options}):").lower()
    if choice == "off":
        turn_off = True
    elif choice == "report":
        coffee_maker.report()  # resources
        money_machine.report()  # profit
    else:
        drink = menu.find_drink(choice)
        if drink is None:
            continue
        elif coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
