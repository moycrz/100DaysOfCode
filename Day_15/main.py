import os
from data import MENU, resources

QUARTER = 0.25
DIME = 0.10
NICKLE = 0.05
PENNIE = 0.01

espresso = MENU.get('espresso')
cappuccino = MENU.get('cappuccino')
latte = MENU.get('latte')

water = resources.get('water')
milk = resources.get('coffee')
coffee = resources.get('milk')

espresso_cost = espresso.get('cost')
latte_cost = latte.get('cost')
cappuccino_cost = cappuccino.get('cost')

money = 0


def supply_check(a, b, c):
    global water
    global milk
    global coffee

    if water < a:
        return "Sorry there is not enough water."
            
    elif milk < b:
        return "Sorry there is not enough milk."
            
    elif coffee < c:
        return "Sorry there is not enough coffee."

    if water == 0 or coffee == 0 or milk== 0:
        return "Out of service, need supply"

    elif water <= 49 or coffee <= 17 or milk <= 99:
        return "Out of service, need supply"

    else:
        milk -= b
        coffee -= c
        water -= a


def money_check(cost, coffee_type):
    global money

    quarters = int(input("how many quarters?: ")) * QUARTER
    dimes = int(input("how many dimes?: ")) * DIME
    nickles = int(input("how many nickles?: ")) * NICKLE
    pennies = int(input("how many pennies?: ")) * PENNIE
    total_money = float(quarters + dimes + nickles + pennies)

    if total_money < cost:
        return "Sorry that's not enough money. Money refunded."

    elif total_money > cost:
        money += cost
        return f"Here is ${round(total_money - cost, 2)} in change." \
               f"Here is your {coffee_type} ☕️. Enjoy!"

    elif total_money == cost:
        money += cost
        return f"Here is your {coffee_type} ☕️. Enjoy!"


def run():
    is_on = True
    while is_on:
        print(f"\tMenu:\nEspresso:\t${espresso_cost}\nLatte:\t\t${latte_cost}\nCappuccino:\t${cappuccino_cost}\n")
        answer = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if answer == "off":
            break

        if answer == "report":
            print(f"Water: {water}ml")
            print(f"Milk: {milk}ml")
            print(f"Coffee: {coffee}g")
            print(f"Money: ${round(money, 2)}")
        
        elif answer == "espresso":
            ingredients = dict(espresso.get('ingredients'))
            c_water = ingredients.get('water')
            c_milk = 0
            c_coffee = ingredients.get("coffee")
            ans = supply_check(c_water, c_milk, c_coffee)

        elif answer == "latte":
            ingredients = dict(latte.get('ingredients'))
            c_water = ingredients.get('water')
            c_milk = ingredients.get('milk')
            c_coffee = ingredients.get("coffee")
            ans = supply_check(c_water, c_milk, c_coffee)

        elif answer == "cappuccino":
            ingredients = dict(cappuccino.get('ingredients'))
            c_water = ingredients.get('water')
            c_milk = ingredients.get('milk')
            c_coffee = ingredients.get("coffee")
            ans = supply_check(c_water, c_milk, c_coffee)


        if type(ans) == str:
            print(ans)
            is_on == False
        
        else:
            if answer == "espresso":
                print("Please insert coins.")
                print(money_check(espresso_cost, "espresso"))

            elif answer == "latte":
                print("Please insert coins.")
                print(money_check(latte_cost, "latte"))
                

            elif answer == "cappuccino":
                print("Please insert coins.")
                print(money_check(cappuccino_cost, "cappuccino"))

  


if __name__ == '__main__':
    os.system('clear')
    run()
