from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True
while is_on:
    coffee_options = menu.get_items()
    user_input = input(f"What would you like? {coffee_options} ").lower()
    if user_input == 'report':
       coffee_maker.report()
       money_machine.report()

    elif user_input == 'off':
        is_on = False
    else:
        drink = menu.find_drink(user_input) # return a menu_item object having name, cost, ingredients
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

    # print(menu_item.name) #latte
    # print(menu_item.cost) #2.5
    # print(menu_item.ingredients)#{'water': 200, 'milk': 150, 'coffee': 24}

