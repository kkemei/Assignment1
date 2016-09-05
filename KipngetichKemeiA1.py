import csv


def main():
    items = open('items.csv')
    csv_file = csv.reader(items)
    items_list = list(csv_file)
    num_of_items = sum(1 for row in items_list)  # calculates how many different items there are
    shopping_list = []

    print("Shopping List 1.0 - by Kipngetich Kemei")
    print("{} items loaded from {}".format(num_of_items, items.name))

    menu_choice = menu()  # calls the main menu function

    while menu_choice != "Q":
        if menu_choice == "R":
            required_items = run_required(num_of_items, items_list)
            menu_choice = menu()  # calls the main menu function
        elif menu_choice == "C":
            completed_items = run_complete(shopping_list, items_list)
            menu_choice = menu()  # calls the main menu function
        # elif menu_choice == "A":
        #     add_items = run_add_new()
        elif menu_choice == "M":
            mark_items = run_mark_item(num_of_items, items_list, shopping_list)
            menu_choice = menu()  # calls the main menu function


def menu():
    menu_options = ['R', 'C', 'A', 'M', 'Q']

    menu_choice = input(
        "Menu: \n R - List required items \n C - List completed items \n A - Add new item \n M - Mark an item as "
        "completed \n Q - Quit")
    menu_choice = menu_choice.upper()

    while menu_choice not in menu_options:  # Error checking for values entered in menu
        print("Invalid option")
        menu_choice = input(
            "Menu: \n R - List required items \n C - List completed items \n A - Add new item \n M - Mark an item as "
            "completed \n Q - Quit\n")
        menu_choice = menu_choice.upper()

    return menu_choice


def run_required(num_of_items, items_list):
    counter = 0
    print("Required items:")
    for row in items_list:
        # items_list[0][2].sort()
        print("{}. {:25} $ {:7} ({})".format(counter, row[0], row[1], row[2]))
        counter += 1

    expected_price = float(items_list[0][1]) + float(items_list[1][1]) + float(items_list[2][1])

    print("total expected price for {} items is: ${}\n".format(num_of_items, expected_price))
    return expected_price


def run_mark_item(num_of_items, items_list, shopping_list):
    number = 0
    for row in items_list:
        # items_list[0][2].sort()
        print("{}. {:25} $ {:7} ({})".format(number, row[0], row[1], row[2]))
        number += 1

    expected_price = float(items_list[0][1]) + float(items_list[1][1]) + float(items_list[2][1])
    print("total expected price for {} items is: ${}".format(num_of_items, expected_price))
    numbers = [0, 1, 2, 3]
    number_to_be_marked = int(input("Enter the number of of an item to mark as completed"))
    if number_to_be_marked not in numbers:
        print("Invalid option")
    shopping_list.append(items_list[number_to_be_marked][0])
    print("{} is marked as complete\n".format(shopping_list[0]))
    return shopping_list


def run_complete(shopping_list, items_list):
    if not shopping_list:
        print("No complete items\n")
    else:
        if shopping_list in items_list:
            # price = float(shopping_list[0][1])
            print("test test test")
            # print("total expected price for {} items is: ${}".format(len(shopping_list), price))

            print(shopping_list)
            print("Completed Items\n")


main()
