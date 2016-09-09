"""
CP1404 Assignment 1 - Shopping List

Kipngetich Kemei
9/9/16
This program allows the user to see a predetermined shopping list , mark items to buy, see what items have been marked
as complete and it also allows the user to add a item to the shopping list.

Github Repository: https://github.com/kkemei/Assignment1

"""

import csv
import operator


def main():  # The main functions that runs the program
    items_list = load_items()

    num_of_items = calculate_numbers(items_list)
    shopping_list = []
    number_to_be_marked = []

    print("Shopping List 1.0 - by Kipngetich Kemei")
    print("{} items loaded from {}".format(num_of_items, "items.csv"))

    menu_choice = menu()  # calls the main menu function

    while menu_choice != "Q":
        if menu_choice == "R":
            num_of_items = calculate_numbers(items_list)
            required_items = run_required(num_of_items, items_list)
            menu_choice = menu()  # calls the main menu function
        elif menu_choice == "M":
            num_of_items = calculate_numbers(items_list)
            mark_items = run_mark_item(num_of_items, items_list, shopping_list, number_to_be_marked)
            menu_choice = menu()  # calls the main menu function
        elif menu_choice == "C":
            num_of_items = calculate_numbers(items_list)
            completed_items = run_complete(shopping_list, items_list, number_to_be_marked)
            menu_choice = menu()  # calls the main menu function
        elif menu_choice == "A":
            num_of_items = calculate_numbers(items_list)
            add_items = run_add_new(items_list)
            menu_choice = menu()  # calls the main menu function
    num_of_items = calculate_numbers(items_list)
    quit_program = run_quit(items_list, num_of_items)


"""
function load_items:
    items = open(csv file)
    csv_file = csv.reader(items)
    items_list = list(csv_file)

    return items_list
"""


def load_items():  # The function that loads in the csv file and passes it back to the main
    items = open('items.csv')
    csv_file = csv.reader(items)
    items_list = list(csv_file)
    return items_list


def calculate_numbers(items_list):  # This function calculates how many items there are currently in the program
    num_of_items = sum(1 for row in items_list)
    return num_of_items


def menu():  # this function is the main menu. Allows the user to access different functions
    menu_options = ['R', 'C', 'A', 'M', 'Q']

    menu_choice = input(
        "Menu: \n R - List required items \n C - List completed items \n A - Add new item \n M - Mark an item as "
        "completed \n Q - Quit\n >>>")
    menu_choice = menu_choice.upper()

    while menu_choice not in menu_options:  # Error checking for values entered in menu
        print("Invalid option")
        menu_choice = input(
            "Menu: \n R - List required items \n C - List completed items \n A - Add new item \n M - Mark an item as "
            "completed \n Q - Quit\n >>>")
        menu_choice = menu_choice.upper()

    return menu_choice


def run_required(num_of_items, items_list):  # This function displays all the items inside the items list
    row_counter = 0
    expected_price_list = []
    print("Required items:")
    items_list.sort(key=operator.itemgetter(2))
    for row in items_list:
        print("{}. {:25} $ {:7} ({})".format(row_counter, row[0], row[1], row[2]))
        expected_price_list.append(float((items_list[row_counter][1])))
        row_counter += 1
    expected_price = sum(expected_price_list)

    print("total expected price for {} items is: ${}\n".format(num_of_items, expected_price))
    return expected_price, items_list


"""
function run_complete(shopping_list, items_list, number_to_be_marked):
    items_counter = 0
    expected_price_list = []

    for each row in items_list:
        print all the items' name, price and priority
        append price to expected_price_list
        items_counter += 1
    sum all the values in expected_prices_list

    display total price expected price of all the items just shown
    get number_entered
    while true
        try:
            get number_entered
            if number_entered not in range(0, num_of_items) or number_entered in number_to_be_marked:
                display Invalid option
            else:
                break
        except ValueError:
            display Invalid input; enter a valid number
    append the number entered to the number to be marked list
    append the item marked to the shopping list
    change the item_required to completed
    display the items that has been marked as completed
    return shopping_list and number_to_be_marked
"""


def run_mark_item(num_of_items, items_list, shopping_list,
                  number_to_be_marked):  # Allows the user to mark a item as complete
    items_counter = 0
    expected_price_list = []
    items_list.sort(key=operator.itemgetter(2))

    for row in items_list:
        print("{}. {:25} $ {:7} ({})".format(items_counter, row[0], row[1], row[2]))
        expected_price_list.append(float((items_list[items_counter][1])))
        items_counter += 1
    expected_price = sum(expected_price_list)

    print("total expected price for {} items is: ${}".format(num_of_items, expected_price))

    while True:
        try:
            number_entered = int(input("Enter the number of of an item to mark as completed\n >>>"))
            if number_entered not in range(0, num_of_items):
                print("Invalid option")
            elif items_list[number_entered][3] == "c":
                print("Item has already been marked, choose another item")
            else:
                break
        except ValueError:
            print("Invalid input; enter a valid number")

    number_to_be_marked.append(number_entered)
    shopping_list.append(items_list[number_entered][0])
    items_list[number_entered][3] = "c"
    print("{} is marked as complete\n".format(shopping_list[-1]))
    return shopping_list, number_to_be_marked


def run_complete(shopping_list, items_list,
                 number_to_be_marked):  # shows all the items that have been marked as complete
    counter = 0
    expected_price_list = []
    num_of_items = sum(1 for row in shopping_list)  # calculates how many different items there are
    items_list.sort(key=operator.itemgetter(2))
    if not shopping_list:
        print("\nNo complete items\n")
    else:
        print("Completed Items:\n")
        for row in shopping_list:
            expected_price_list.append(float((items_list[number_to_be_marked[counter]][1])))
            print("{}. {:25} $ {} ({})".format(counter, shopping_list[counter],
                                               items_list[number_to_be_marked[counter]][1],
                                               items_list[number_to_be_marked[counter]][2]))
            counter += 1
        expected_price = sum(expected_price_list)
        print("total expected price for {} items is: ${}".format(num_of_items, expected_price))

    return shopping_list


def run_add_new(items_list):  # allows the user to add a item to the programs item list
    priority_list = ["1", "2", "3"]
    item_name = str(input("Please enter a item name:\n >>>"))
    while not item_name:
        print("Input can not be blank")
        item_name = input("Please enter a item name:")

    while True:
        try:
            item_price = int(input("Item Price:\n >>>"))
            if item_price < 0:
                print("Invalid input; Price must be greater that 0")
            else:
                break
        except ValueError:
            print("Invalid input; enter a valid number")

    item_priority = input("Please enter the items priority:\n >>>")
    while item_priority not in priority_list:
        print("Invalid input; Priority must be either 1, 2 or 3")
        item_priority = input("Please enter the items priority:\n >>>")

    item_required = "r"

    items_list.append([item_name, float(item_price), item_priority, item_required])
    print("{}, ${}, priority ({}) added to shopping list".format(item_name, float(item_price), item_priority))
    return items_list


def run_quit(items_list, num_of_items):  # runs when the user quits and prints all the items to the csv
    with open('items.csv', "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(items_list)
    print("{} items saved to items.csv \n"
          "Have a nice day :)".format(num_of_items))


main()
