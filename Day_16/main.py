from prettytable import PrettyTable

from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

is_on = True
coffee_machine = CoffeeMaker()
m_item = Menu()
money_machine = MoneyMachine()

menu_table = PrettyTable()
menu_table.add_column("Coffee", ["Espresso", "Latte", "Cappuccino"])
menu_table.add_column("Price", ["$1.5", "$2.5", "$3"])

espresso = MenuItem("espresso", 50, 0, 18, 1.5)
latte = MenuItem("latte", 200, 150, 24, 2.5)
cappuccino = MenuItem("cappuccino", 250, 50, 24, 3)


def ingredients(coffee_choice):
    return coffee_choice.ingredients


def cost(coffee_type):
    return coffee_type.cost


while is_on:
    print(menu_table)
    choice = input("What would you like? (espresso/latte/cappuccino/): ").lower()

    if choice == "off":
        is_on = False

    elif choice == "report":
        coffee_machine.report()
        money_machine.report()

    elif choice == "espresso":
        if coffee_machine.is_resource_sufficient(espresso):
            price = cost(espresso)
            if money_machine.make_payment(price):
                coffee_machine.make_coffee(espresso)
            else:
                continue

    elif choice == "latte":
        if coffee_machine.is_resource_sufficient(latte):
            price = cost(latte)
            if money_machine.make_payment(price):
                coffee_machine.make_coffee(latte)
            else:
                continue

    elif choice == "cappuccino":
        if coffee_machine.is_resource_sufficient(cappuccino):
            price = cost(cappuccino)
            if money_machine.make_payment(price):
                coffee_machine.make_coffee(cappuccino)
            else:
                continue
