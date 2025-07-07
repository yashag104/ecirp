from cm_data import MENU
from cm_data import resources
from os import system
system('cls')
QUARTERS = 0.25
DIMES = 0.1
PENNIES = 0.01
NICKLES = 0.05


def money(quarters, dimes, pennies, nickles):
    return quarters*QUARTERS+dimes*DIMES+pennies*PENNIES+nickles*NICKLES


def coffee(choice, coin):
    if choice == "report":
        print(resources)
    else:
        change = round(coin-(MENU[choice]['cost']), 2)
        if change < 0:
            print("You gave insufficient amount of money.")
            print(f"Here is ${coin}. Money Refunded.")
        else:
            print(f"Here is ${change} in change.")
            print(f"Here is you {choice}. Enjoy!")
        resources['water'] -= (MENU[choice]['ingredients']['water'])
        resources['milk'] -= (MENU[choice]['ingredients']['milk'])
        resources['coffee'] -= (MENU[choice]['ingredients']['coffee'])
        return MENU[choice]['cost']


switch = True
earned = 0
while switch:
    choice = input("What would you like? (espresso/latte/cappuccino)")
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if not resources['water'] >= MENU[choice]['ingredients']['water'] or not resources['milk'] >= MENU[choice]['ingredients']['milk'] or not resources['coffee'] >= MENU[choice]['ingredients']['coffee']:
            print("Insufficient ingredients. Sorry")
        else:
            print("Please enter the number of coins")
            quarter = int(input("No of quarter: "))
            dime = int(input("No of dimes: "))
            penny = int(input("No of pennies: "))
            nickle = int(input("No of nickles: "))
            coins = money(quarter, dime, penny, nickle)
            earned += coffee(choice, coins)
    elif choice == "report":
        coins = 0
        coffee(choice, coins)
    elif choice == "off":
        switch = False
        print(f"Total money earned is ${earned}.")
        earned = 0
    else:
        print("Please enter a valid option.")
