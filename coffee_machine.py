import coffee_machine_menu

def calculate_money(quarters,dimes,nickles,pennies,coins):
    total_value = coins["quarter"] * quarters
    total_value+=coins["dime"] * dimes
    total_value+=coins["nickel"] * nickles
    total_value+=coins["penny"] * pennies
    return total_value

def check_transaction(value,menu,coffee):
    if value >= menu[coffee]["cost"]:
        return True
    else:
        return False
    
def process_coins(value,menu,coffee):
    change = round(value - menu[coffee]["cost"],2)
    return f'Here is $ {change} in change.'

def print_report(resources,money):
    print(f'Water: {resources["water"]}ml.')
    print(f'Milk: {resources["milk"]}ml.')
    print(f'Coffee: {resources["coffee"]}g.')
    print(f'Money: $ {money}.')

def check_resources(coffee,resources,menu):
    water_resources = resources["water"]
    milk_resources = resources["milk"]
    coffee_resources = resources["coffee"]
    if coffee == "espresso":
        if menu[coffee]["ingredients"]["water"] > water_resources:
            return "water"
        if menu[coffee]["ingredients"]["coffee"] > coffee_resources:
            return "coffee"
    else:
        if menu[coffee]["ingredients"]["water"] > water_resources:
            return "water"
        if menu[coffee]["ingredients"]["milk"] > milk_resources:
            return "milk"
        if menu[coffee]["ingredients"]["coffee"] > coffee_resources:
            return "coffee"
        
def calculate_resources(coffee,menu,resources):
    if coffee == "espresso":
        resources["water"] = resources["water"] - menu[coffee]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - menu[coffee]["ingredients"]["coffee"]
    else:
        resources["water"] = resources["water"] - menu[coffee]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - menu[coffee]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - menu[coffee]["ingredients"]["coffee"]
    return resources
    
def running_coffee_machine():
    coffee_machine_is_on = True
    money_machine = 0
    resources = coffee_machine_menu.resources
    menu = coffee_machine_menu.MENU
    coins = coffee_machine_menu.coins
    while coffee_machine_is_on:
        coffee_type = input("What would you like? (espresso/latte/cappuccino):").lower().strip()
        if coffee_type == "report":
            print_report(resources = resources,money=money_machine)
        elif coffee_type == "off":
            coffee_machine_is_on = False
        else:
            are_there_resources = check_resources(coffee=coffee_type,resources=resources,menu=menu)
            if are_there_resources == None:
                print("Please insert coins.")
                quarters_quantity = int(input("How many quarters? ").strip())
                dimes_quantity = int(input("How many dimes? ").strip())
                nickles_quantity = int(input("How many nickles? ").strip())
                penny_quantity = int(input("How many pennies? ").strip())
                total_value = calculate_money(quarters=quarters_quantity,dimes=dimes_quantity,nickles=nickles_quantity,pennies=penny_quantity,coins=coins)
                transaction_status = check_transaction(value=total_value,menu=menu,coffee=coffee_type)
                if transaction_status:
                    print(process_coins(value=total_value,menu=menu,coffee = coffee_type))
                    print(f"Here is your {coffee_type}. Enjoy!")
                    money_machine+=menu[coffee_type]["cost"]
                    resources = calculate_resources(resources=resources,menu=menu,coffee = coffee_type)
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print(f'Sorry there is not enough {are_there_resources}.')

running_coffee_machine()






    


