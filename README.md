# Coffee Machine Project

This is a simple project that simulates a coffee machine in Python.
The machine offers three types of drinks: espresso, latte, and cappuccino.
The user can insert coins to buy a drink and the machine checks if there are sufficient resources to prepare the chosen drink.

## Features

**Report:** Displays the current amount of water, milk, coffee, and money in the machine.
**Turn Off:** Turns off the coffee machine.
**Drink Purchase:** Allows the user to choose between espresso, latte, or cappuccino and pay with coins.

## How to Use

**Start the machine:** When starting the script `running_coffee_machine()`, the machine will begin operating and ask the user to choose an action.

**Choose a drink:** The user can choose between espresso, latte, or cappuccino.

**Insert coins:** If the drink is available, the machine will ask the user to insert coins. The user must provide the quantity of each type of coin (quarters, dimes, nickels, pennies).

**Transaction processing:** The machine checks if the amount of money inserted is sufficient for the purchase. If so, the machine provides the drink and change, if any. If not, the machine informs that the money is insufficient and returns the coins.

**Report:** At any time, the user can type `report` to see the current amount of resources in the machine.

**Turn off the machine:** The user can type `off` to turn off the machine.

## Functions

**`calculate_money(quarters, dimes, nickels, pennies, coins)`:** Calculates the total value of money inserted based on the quantities of each type of coin.

**`check_transaction(value, menu, coffee)`:** Checks if the inserted value is sufficient to buy the chosen drink.

**`process_coins(value, menu, coffee)`:** Calculates and returns the change to be returned to the user.

**`print_report(resources, money)`:** Displays a report of current resources and money in the machine.

**`check_resources(coffee, resources, menu)`:** Checks if there are sufficient resources to prepare the chosen drink.

**`calculate_resources(coffee, menu, resources)`:** Updates the machine's resources after preparing a drink.

**`running_coffee_machine()`:** Main function that controls the coffee machine's execution.

## Imports

The code imports the `coffee_machine_menu` module, which defines the initial resources, drink menu, and coin values.

## Menu Structure

The `coffee_machine_menu` module contains a `MENU` dictionary with the structure of drinks and their respective costs and ingredients, a `resources` dictionary with the initial amount of water, milk, and coffee, and a `coins` dictionary with coin values.