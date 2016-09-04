import csv

def main():
    items = open('items.csv')
    csv_file = csv.reader(items)
    items_list = list(csv_file)
    num_of_items = sum(1 for row in items)  # calculates how many different items there are

    menu_choice = menu(items, num_of_items) #calls the main function

    if menu_choice == "R":
        required_items = run_required(num_of_items, items_list)
    # elif menu_choice == "C":
    #     completed_items = run_complete()
    # elif menu_choice == "A":
    #     add_items = run_add_new()
    # elif menu_choice == "M":
    #     mark_items = run_mark item()

def run_required(num_of_items, items_list):
    x = 0

    print(items_list)

    print("Required items:\n")
    for row in items_list:
        # items_list.sort()
        print("{}. {:25} $ {:7} ({})".format(x, row[0], row[1], row[2]))
        x += 1

    expected_price = float(items_list[0][1]) + float(items_list[1][1]) + float(items_list[2][1])

    print("total expected price for {} items is: ${}".format(num_of_items, expected_price))


def menu(items, num_of_items):
    print("Shopping List 1.0 - by Kipngetich Kemei")
    print("{} items loaded from {}".format(num_of_items, items.name))

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
