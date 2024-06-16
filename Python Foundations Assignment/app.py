import datetime
import time

from model import Items


def run_app():
    Items.load_from_file()
    while True:
        print("Python Collector")
        print("----------------")
        print("1. Add Item to Collection.")
        print("2. Show Items in Collection.")
        print("3. Delete Items from Collection.")
        print("4. Exit")
        while True:
            try:
                user_input = int(input("Choice> "))
            except ValueError:
                print("Invalid input, please enter a number")
                continue

            if user_input == 1:
                add_items()
                break
            elif user_input == 2:
                show_items()
                break
            elif user_input == 3:
                delete_items()
                break
            elif user_input == 4:
                return
            else:
                print("Invalid choice, try again.")


def add_items():
    print()
    print("Adding an Item")
    print("--------------")
    title = input("Title> ")
    print("Types: 1. Computer, 2. Camera, 3. Phone, 4. Video Player")
    while True:
        try:
            item_type = int(input("Type> "))
            if item_type not in [1, 2, 3, 4]:
                print("Invalid type. Please choose from the provided options.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    current_date = datetime.datetime.now()
    while True:
        date_added = input("Date Added (DD-MM-YYYY)> ")
        try:
            date_added = datetime.datetime.strptime(date_added, "%d-%m-%Y")
            if date_added > current_date:
                print("Date cannot be in the future.")
            else:
                break
        except ValueError:
            print("Invalid date format. Please use the DD-MM-YYYY format.")

    while True:
        date_of_manufacture = input("Date of Manufacture (DD-MM-YYYY)> ")
        try:
            date_of_manufacture = datetime.datetime.strptime(date_of_manufacture, "%d-%m-%Y")
            if date_of_manufacture > current_date:
                print("Date cannot be in the future.")
            elif date_of_manufacture > date_added:
                print("Date of manufacture cannot be after the date added.")
            else:
                break
        except ValueError:
            print("Invalid date format. Please use the DD-MM-YYYY format.")

    description = input("Description> ")

    date_added_str = date_added.strftime("%d-%m-%Y")
    date_of_manufacture_str = date_of_manufacture.strftime("%d-%m-%Y")

    Items(title, item_type, date_added_str, date_of_manufacture_str, description)
    print("Item added successfully!")
    Items.save_to_file()
    print()
    time.sleep(1)


def show_items():
    if len(Items.ITEMS) == 0:
        print("There are no items to view. Returning to main menu.")
        time.sleep(1)
        return

    print()
    while True:
        print("Types: 1. Computer, 2. Camera, 3. Phone, 4. Video Player")
        user_input = int(input("Type> "))
        if user_input == 1:
            print("Showing: Computer")
            if len(Items.ITEMS) == 0:
                print("There are no items to view. Returning to main menu.")
                return
        elif user_input == 2:
            print("Showing: Camera")
            if len(Items.ITEMS) == 0:
                print("There are no items to view. Returning to main menu.")
                return
        elif user_input == 3:
            print("Showing: Phone")
            if len(Items.ITEMS) == 0:
                print("There are no items to view. Returning to main menu.")
                return
        elif user_input == 4:
            print("Showing: Video Player")
            if len(Items.ITEMS) == 0:
                print("There are no items to view. Returning to main menu.")
                return
        else:
            print("Invalid choice, please try again.")
            break
        print("{:<20}\t{:<20}\t{:<20}".format("Item", "Date Added", "Date of Manufacture"))
        found_items = False
        for i in Items.ITEMS:
            if i.type == user_input:
                found_items = True
                print("{:<20}\t{:<20}\t{:<20}".format(i.title, i.date_added, i.date_manufactured))
                print("----------END OF LIST----------")

        if not found_items:
            print("No items of this type are available. Returning to main menu.")
            print()
            time.sleep(1)
        break


def delete_items():
    if len(Items.ITEMS) == 0:
        print("There are no items to view. Returning to main menu.")
        time.sleep(1)
        return
    print("What would you like to delete? Press 'c' to cancel.")
    print("{:<10}\t{:<20}".format("Number", "Item"))
    for id, i in enumerate(Items.ITEMS, start=1):
        print("{:<10}\t{:<20}".format(id, i.title))

    while True:
        try:
            choice = input("Delete (press 'c' to cancel)> ")
            if choice.lower() == 'c':
                print("Operation canceled.")
                return
            else:
                item_to_delete = int(choice)
                if 1 <= item_to_delete <= len(Items.ITEMS):
                    break
                else:
                    print("Please enter a valid item number.")
        except ValueError:
            print("Please enter a valid choice.")

    item_to_delete = Items.ITEMS.pop(item_to_delete - 1)
    print(f"{item_to_delete.title} has been deleted")


run_app()
