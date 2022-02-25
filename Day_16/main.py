from prettytable import PrettyTable

import money_machine
from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

is_on = True
coffee_machine = CoffeeMaker()
# m_item = Menu.find_drink(choice)
# print(m_item.cost())

menu_table = PrettyTable()
menu_table.add_column("Coffee", ["Espresso", "Latte", "Cappuccino"])
# menu_table.add_column("Price", [m_item("espresso"), m_item("latte"), m_item("cappuccino")])

current_money = MoneyMachine

while is_on:
    # print(menu_table)
    choice = input("What would you like? (espresso/latte/cappuccino/): ")

    if choice == "off":
        is_on = False

    elif choice == "report":
        coffee_machine.report()
        print(MoneyMachine.report())

    elif choice == "espresso":
        if coffee_machine.is_resource_sufficient(choice):
            coffee_machine.make_coffee(choice)
        m_item = Menu.find_drink(choice)
        print(m_item.cost())

    elif choice == "latte":
        if coffee_machine.is_resource_sufficient(choice):
            coffee_machine.make_coffee(choice)

    elif choice == "cappuccino":
        if coffee_machine.is_resource_sufficient(choice):
            coffee_machine.make_coffee(choice)
