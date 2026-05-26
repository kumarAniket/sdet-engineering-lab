from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


class CoffeeMachine:
    """Models the machine that makes the coffee"""

    money_machine = MoneyMachine()
    money_machine.report()
    print()
    print("-- Resources Before--")
    coffee_maker = CoffeeMaker()
    coffee_maker.report()
    print("---------------")
    print()
    order_menu = Menu()

    while True:
        customer_order = input(f"What would you like? ({order_menu.get_items()}):")

        if customer_order.lower()=='off':
            break
        elif (coffee_maker.is_resource_sufficient(order_menu.find_drink(customer_order)) and
              money_machine.make_payment(order_menu.find_drink(customer_order).cost)):
            coffee_maker.make_coffee(order_menu.find_drink(customer_order))
            print()
            print("--- Final Report ---")
            money_machine.report()
            coffee_maker.report()
            print("--------------------")
