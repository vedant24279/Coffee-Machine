MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def coins():
    """Returns Total of money received"""
    print("Please insert coins")
    total_paid = int(input("How Many Quarters :")) * 0.25
    total_paid += int(input("How Many Dimes :")) * 0.1
    total_paid += int(input("How Many Nickles :")) * 0.05
    total_paid += int(input("How Many Pennies :")) * 0.01
    return total_paid

def is_transaction_successful(money_received,coffee_cost):
    """check if the transaction is successful or not"""
    if money_received < coffee_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif money_received > coffee_cost:
        global profit
        profit += coffee_cost
        change = round(money_received - coffee_cost,2)
        print(f"Here is your change ${change}")
        return True




def is_resource_sufficient(order_ingredients):
    """Return True if the resource is available and False if not."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def resource_updater(coffee_name,ingredients):
    """Deduct the ingredients from resources."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {coffee_name} enjoy!☕")

coffee_machine = True

while coffee_machine:
    user_choice = str(input("What would you like? (espresso/latte/cappuccino):")).lower()
    if user_choice == "off":
        coffee_machine = False
    elif user_choice == "report":
        print(F"Water : {resources["water"]}\nMilk : {resources["milk"]}\nCoffee : {resources["coffee"]}\nMoney : ${profit}")
    else:
        drink =  MENU[user_choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = coins()
            if is_transaction_successful(payment,drink["cost"]):
                resource_updater(user_choice,drink["ingredients"])