MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    "money": 0,
}


def calculate_coffee(coffee_machine):
    if resources['water'] < MENU[coffee_machine]['ingredients']['water']:
        print("Sorry there is not enough water.")
    elif resources['coffee'] < MENU[coffee_machine]['ingredients']['coffee']:
        print("Sorry there is not enough coffee.")
    elif resources['milk'] < MENU[coffee_machine]['ingredients']['milk']:
        print("Sorry there is not enough milk.")
    else:
        print(f"Please, insert the coins! Cost: {MENU[coffee_machine]['cost']}\n")
        quarters = 0.25 * float(input("How many quarters?\n"))
        dimes = 0.10 * float(input("How many dimes?\n"))
        nickels = 0.05 * float(input("How many nickels?\n"))
        pennies = 0.01 * float(input("How many pennies?\n"))
        coins = quarters + dimes + nickels + pennies
        if coins < MENU[coffee_machine]['cost']:
            print("Sorry that's not enough money. Money refunded.")
        elif coins > MENU[coffee_machine]['cost']:
            refund = round(coins - MENU[coffee_machine]['cost'])
            print(f"Here is ${refund} dollars in change")
            resources['money'] += coins - refund
        else:
            resources['money'] += coins
            resources['water'] -= MENU[coffee_machine]['ingredients']['water']
            resources['coffee'] -= MENU[coffee_machine]['ingredients']['coffee']
            resources['milk'] -= MENU[coffee_machine]['ingredients']['milk']
        print(f"Here is your {coffee_machine}!\n")


state_machine = True

while state_machine:
    machine = input("What would you like? (espresso / latte / cappuccino):")
    if machine == "off":
        state_machine = False
        break
    elif machine == 'espresso' or machine == 'latte' or machine == 'cappuccino':
        calculate_coffee(machine)
    elif machine == "report":
        print(
            f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \nMoney ${round(resources['money'], 2)}\n")
