MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def deduct_resources(coffee):
    """
    deducts the appropriate amount of resources from the coffee machine
    as they were used in making the coffee
    :param coffee:
    :return:
    """
    c_water = MENU[coffee]['ingredients']['water']
    c_milk = MENU[coffee]['ingredients']['milk']
    c_coffee = MENU[coffee]['ingredients']['coffee']

    # deducting the resources used to make coffee from the machine
    resources['water'] -= c_water
    resources['milk'] -= c_milk
    resources['coffee'] -= c_coffee


def check_resources(coffee_type):
    """
    checks if the user's desired coffee can be made based on the resources
    available and resources required
    :param coffee_type:
    :return:
    """
    coffee = coffee_type
    r_water = resources['water']
    r_milk = resources['milk']
    r_coffee = resources['coffee']
    c_water = MENU[coffee]['ingredients']['water']
    c_milk = MENU[coffee]['ingredients']['milk']
    c_coffee = MENU[coffee]['ingredients']['coffee']

    # if enough ingredients are available then return true
    if r_water >= c_water and r_milk >= c_milk and r_coffee >= c_coffee:
        return True
    # if there aren't enough resources then notify the user about
    # which resource(s) are lacking
    else:
        if r_water < c_water:
            print("Sorry, There isn't enough water.")
        if r_milk < c_milk:
            print("Sorry, There isn't enough milk.")
        if r_coffee < c_coffee:
            print("Sorry, There isn't enough coffee.")

        return False


def check_money(quarters, dimes, nickels, pennies, coffee):
    """
    checks if the money inserted by the user is enough to buy the
    coffee wanted by the user
    :param coffee:
    :param quarters:
    :param dimes:
    :param nickels:
    :param pennies:
    :return:
    """
    total_money = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    c_cost = MENU[coffee]['cost']

    # if user inserted enough money then return true
    if total_money >= c_cost:
        return True
    # if money isn't enough then notify the user
    else:
        print("Not enough money")
        print("Money refunded")
        return False


def main():
    """
    manages the main functionality of the coffee machine
    :return:
    """
    should_continue = True
    money = 0
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    # main loop
    while should_continue:

        user_input = input("What would you like? (espresso/latte/cappuccino): ")

        if user_input == "off":
            should_continue = False

        # if user wants a report
        elif user_input == "report":
            print(f"Water: {resources['water']}")
            print(f"Milk: {resources['milk']}")
            print(f"Coffee: {resources['coffee']}")
            print(f"Money: {money}")

        # if they enter a coffee type
        elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
            if check_resources(user_input):
                print("Please insert coins:")

                quarters = int(input("How many quarters? "))
                dimes = int(input("How many dimes? "))
                nickels = int(input("How many nickels? "))
                pennies = int(input("How many pennies? "))

                total_money = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

                if check_money(quarters, dimes, nickels, pennies, user_input):
                    money += total_money

                    change = total_money - MENU[user_input]['cost']
                    print(f"Here is ${round(change, 2)} dollars in change.")

                    deduct_resources(user_input)

                    print(f"Here is your {user_input}, enjoy.")

                else:
                    continue
            else:
                continue


if __name__ == '__main__':
    main()