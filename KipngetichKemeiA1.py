import csv
import operator


def main():
    items = open('items.csv')
    csv_file = csv.reader(items)
    items_list = list(csv_file)
    num_of_items = sum(1 for row in items_list)  # calculates how many different items there are
    shopping_list = []
    number_to_be_marked = []

    print("Shopping List 1.0 - by Kipngetich Kemei")
    print("{} items loaded from {}".format(num_of_items, items.name))

    menu_choice = menu()  # calls the main menu function

    while menu_choice != "Q":
        if menu_choice == "R":
            required_items = run_required(num_of_items, items_list)
            menu_choice = menu()  # calls the main menu function
        elif menu_choice == "A":
            add_items = run_add_new()
            menu_choice = menu()  # calls the main menu function
        elif menu_choice == "M":
            mark_items = run_mark_item(num_of_items, items_list, shopping_list, number_to_be_marked)
            menu_choice = menu()  # calls the main menu function
        elif menu_choice == "C":
            completed_items = run_complete(shopping_list, items_list, number_to_be_marked)
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
    ##### GET IT TO LOOP THROUGH AND PRINT THE ROW SO THAT IT CAN HANDLE MORE THAN 3 ROWS
    expected_price_list = []
    print("Required items:")
    items_list.sort(key=operator.itemgetter(2))
    for row in items_list:
        print("{}. {:25} $ {:7} ({})".format(counter, row[0], row[1], row[2]))
        expected_price_list.append(float((items_list[counter][1])))
        counter += 1
    expected_price = sum(expected_price_list)

    # expected_price_list = float(items_list[0][1]) + float(items_list[1][1]) + float(items_list[2][1])

    print("total expected price for {} items is: ${}\n".format(num_of_items, expected_price))
    return expected_price

def run_mark_item(num_of_items, items_list, shopping_list, number_to_be_marked):

    ###### GET IT TO PRINT OUT THE RIGHT NAME AFTER A INPUT

    number = 0
    expected_price_list = []
    items_list.sort(key=operator.itemgetter(2))
    for row in items_list:
        print("{}. {:25} $ {:7} ({})".format(number, row[0], row[1], row[2]))
        expected_price_list.append(float((items_list[number][1])))
        number += 1
    expected_price = sum(expected_price_list)

    print("total expected price for {} items is: ${}".format(num_of_items, expected_price))
    numbers = [0, 1, 2]
    number_entered = int(input("Enter the number of of an item to mark as completed"))
    while number_entered not in numbers:
        print("Invalid option")
        number_entered = int(input("Enter the number of of an item to mark as completed"))
    number_to_be_marked.append(number_entered)
    shopping_list.append(items_list[number_entered][0])
    print("{} is marked as complete\n".format(shopping_list[0]))
    return shopping_list, number_to_be_marked

def run_complete(shopping_list, items_list, number_to_be_marked):
    counter = 0
    expected_price_list = []
    num_of_items = sum(1 for row in shopping_list)  # calculates how many different items there are
    items_list.sort(key=operator.itemgetter(2))
    if not shopping_list:
        print("\nNo complete items\n")
    else:
        print("Completed Items:\n")
        for row in shopping_list:
            expected_price_list.append(float((items_list[counter][1])))
            print("{}. {:25} $ {} ({})".format(counter, shopping_list[counter], items_list[number_to_be_marked[counter]][1],
                                               items_list[number_to_be_marked[counter]][2]))
            # print("{}. {}".format(counter, shopping_list))
            counter += 1
        expected_price = sum(expected_price_list)
        print("total expected price for {} items is: ${}".format(num_of_items, expected_price))

def run_add_new():
    # item_name = input("Please enter a item name:")
    # while not item_name:
    print("test")



main()
