import csv

def main():
    items = open('items.csv')
    csv_file = csv.reader(items)
    items_list = list(csv_file)
    num_of_items = sum(1 for row in items_list)  # calculates how many different items there are

    print("Shopping List 1.0 - by Kipngetich Kemei")
    print("{} items loaded from {}".format(num_of_items, items.name))

    menu_choice = menu(items)  # calls the main menu function

    while menu_choice != "Q":
        if menu_choice == "R":
            required_items = run_required(num_of_items, items_list)
            menu_choice = menu(items)  # calls the main menu function
        # elif menu_choice == "C":
        #     completed_items = run_complete()
        # elif menu_choice == "A":
        #     add_items = run_add_new()
        elif menu_choice == "M":
            mark_items = run_mark_item(num_of_items, items_list)
            menu_choice = menu(items)  # calls the main menu function

def run_required(num_of_items, items_list):
    number = 0
    print("Required items:")
    for row in items_list:
        # items_list[0][2].sort()
        print("{}. {:25} $ {:7} ({})".format(number, row[0], row[1], row[2]))
        number += 1

    expected_price = float(items_list[0][1]) + float(items_list[1][1]) + float(items_list[2][1])

    print("total expected price for {} items is: ${}".format(num_of_items, expected_price))


def run_mark_item(num_of_items, items_list):
    number = 0
    for row in items_list:
        # items_list[0][2].sort()
        print("{}. {:25} $ {:7} ({})".format(number, row[0], row[1], row[2]))
        number += 1

    expected_price = float(items_list[0][1]) + float(items_list[1][1]) + float(items_list[2][1])
    print("total expected price for {} items is: ${}".format(num_of_items, expected_price))

    numbers = [0,1,2,3]
    shoppping_list = []
    number_to_be_marked= int(input("Enter the number of of an item to mark as completed"))
    if number_to_be_marked not in numbers:
        print("Invalid option")
    shoppping_list.append(items_list[number_to_be_marked][0])
    print("{} is marked as complete".format(shoppping_list[0]))






def menu(items):

    menu_options = ['R', 'C', 'A', 'M', 'Q']

    menu_choice = input(
        "Menu: \n R - List required items \n C - List completed items \n A - Add new item \n M - Mark an item as "
        "completed \n Q - Quit")
    menu_choice = menu_choice.upper()

    while menu_choice not in menu_options:  # Error checking for values entered in menu
        print("Invalid option")
        menu_choice = input(
            "Menu: \n R - List required items \n C - List completed items \n A - Add new item \n M - Mark an item as "
            "completed \n Q - Quit")
        menu_choice = menu_choice.upper()

    return menu_choice

main()
