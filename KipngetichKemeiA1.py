import csv

def main():
    items = open('items.csv')
    csv_items = csv.reader(items)

    menu_choice =menu(items) #calls the main function
    print(menu_choice)



def menu(items):
    num_of_items = sum(1 for row in items)  # calculates how many different items there are

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
