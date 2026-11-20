import os
import time
import sys

# Initialize the artefact management system using a list
# Each artefact contains: Name, Category, Display Location, Condition

artefact_list = [
    ["Roman Coin", "Coin", "Display Case A", "Good"],
    ["Old Photograph", "Photograph", "Archive Box 1", "Good"],
    ["Handwritten Letter 1940", "Document", "Archive Box 2", "Damaged"],
    ["Victorian Pocket Watch", "Timepiece", "Display Case B", "Under Repair"],
    ["Ancient Pottery Vase", "Pottery", "Display Case C", "Good"],
    ["World War II Medal", "Medal", "Display Case D", "Good"],
    ["Historical Map", "Document", "Archive Box 3", "Damaged"],
    ["Bronze Sculpture", "Sculpture", "Display Case E", "Good"],
    ["Antique Wooden Clock", "Timepiece", "Storage Room A", "Under Repair"],
    ["Traditional Farming Tool", "Tool", "Storage Room B", "Good"]
]


def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_menu():
    """Displays the main menu options."""

    print("\n--- Artefact Management System ---")
    print("1. Add Artefact")
    print("2. Update Artefact Condition")
    print("3. View Artefacts")
    print("4. Search Artefact")
    print("5. Delete Artefact")
    print("6. Update Artefact Details")
    print("7. Count Artefacts")
    print("8. Filter by Category")
    print("9. Filter by Condition")
    print("10. Exit System")
    print("----------------------------------")


def add_artefact():
    """Allows the user to add a new artefact."""

    clear_screen()

    print("\n--- Add Artefact ---")

    artefact_name = input("Enter artefact name: ").strip()
    category = input("Enter artefact category: ").strip()
    display_location = input("Enter display location: ").strip()
    condition = input(
        "Enter condition (Good, Damaged, Under Repair): "
    ).strip()

    if (artefact_name != "" and
            category != "" and
            display_location != "" and
            condition in ["Good", "Damaged", "Under Repair"]):

        artefact = [
            artefact_name,
            category,
            display_location,
            condition
        ]

        artefact_list.append(artefact)

        print("\nArtefact Added")

    else:
        print("\nInvalid Details. Please Try Again.")

    time.sleep(2)


def update_condition():
    """Allows the user to update an artefact's condition."""

    clear_screen()

    print("\n--- Update Artefact Condition ---")

    search_name = input("Enter artefact name: ").strip()

    artefact_found = False

    for artefact in artefact_list:

        if artefact[0].lower() == search_name.lower():

            artefact_found = True

            new_condition = input(
                "Enter new condition (Good, Damaged, Under Repair): "
            ).strip()

            if new_condition in ["Good", "Damaged", "Under Repair"]:

                artefact[3] = new_condition

                print("\nCondition Updated")

            else:
                print("\nInvalid Condition")

            break

    if not artefact_found:
        print("\nArtefact Not Found")

    time.sleep(2)


def view_artefacts():
    """Displays all artefacts stored in the system."""

    clear_screen()

    print("\n--- View Artefacts ---")

    if len(artefact_list) == 0:

        print("\nNo Artefacts Stored")

    else:

        for artefact in artefact_list:

            print("\nArtefact Name:", artefact[0])
            print("Category:", artefact[1])
            print("Display Location:", artefact[2])
            print("Condition:", artefact[3])
            print("----------------------------------")

    input("\nPress Enter to return to the menu...")


def search_artefact():
    """Allows the user to search for an artefact by name."""

    clear_screen()

    print("\n--- Search Artefact ---")

    search_name = input("Enter artefact name to search: ").strip()

    artefact_found = False

    for artefact in artefact_list:

        if artefact[0].lower() == search_name.lower():

            artefact_found = True

            print("\nArtefact Name:", artefact[0])
            print("Category:", artefact[1])
            print("Display Location:", artefact[2])
            print("Condition:", artefact[3])

            break

    if not artefact_found:
        print("\nArtefact Not Found")

    time.sleep(2)


def delete_artefact():
    """Allows the user to delete an artefact."""

    search_name = input("Enter artefact name to delete: ").strip()

    artefact_found = False

    record_position = -1

    for index, artefact in enumerate(artefact_list):
        if artefact[0].lower() == search_name.lower():
            artefact_found = True
            record_position = index
            break

    if artefact_found:
        confirmation = input("Are you sure you want to delete an artefact? (y/n):").strip()
        if confirmation.lower() == "yes":
            artefact_list.pop(record_position)
            print("\nArtefact Deleted")
        else:
            print("\nDeletion cancelled")

    else:
        print("\nArtefact Not Found")









    time.sleep(2)


def update_artefact_details():
    """Allows the user to update an artefact's category and location."""

    clear_screen()

    print("\n--- Update Artefact Details ---")

    search_name = input("Enter artefact name: ").strip()

    artefact_found = False

    for artefact in artefact_list:

        if artefact[0].lower() == search_name.lower():

            artefact_found = True

            new_category = input("Enter new category: ").strip()
            new_location = input("Enter new display location: ").strip()

            if new_category != "" and new_location != "":

                artefact[1] = new_category
                artefact[2] = new_location

                print("\nDetails Updated")

            else:
                print("\nInvalid Details. Please Try Again.")

            break

    if not artefact_found:
        print("\nArtefact Not Found")

    time.sleep(2)


def count_artefacts():
    """Displays the total number of artefacts."""

    clear_screen()

    print("\n--- Count Artefacts ---")

    total_artefacts = len(artefact_list)

    print("\nTotal Number of Artefacts:", total_artefacts)

    time.sleep(2)


def filter_by_category():
    """Displays artefacts matching a selected category."""

    clear_screen()

    print("\n--- Filter by Category ---")

    selected_category = input("Enter category: ").strip()

    match_found = False

    for artefact in artefact_list:

        if artefact[1].lower() == selected_category.lower():
            match_found = True

            print("\nArtefact Name:", artefact[0])
            print("Category:", artefact[1])
            print("Display Location:", artefact[2])
            print("Condition:", artefact[3])
            print("----------------------------------")

    if not match_found:
        print("\nNo Matching Artefacts Found")

    input("\nPress Enter to return to the menu...")


def filter_by_condition():
    """Displays artefacts matching a selected condition."""

    clear_screen()

    print("\n--- Filter by Condition ---")

    selected_condition = input(
        "Enter condition (Good, Damaged, Under Repair): "
    ).strip()

    match_found = False

    if selected_condition not in ["Good", "Damaged", "Under Repair"]:

        print("\nInvalid Condition")

    else:

        for artefact in artefact_list:

            if artefact[3] == selected_condition:
                match_found = True

                print("\nArtefact Name:", artefact[0])
                print("Category:", artefact[1])
                print("Display Location:", artefact[2])
                print("Condition:", artefact[3])
                print("----------------------------------")

        if not match_found:
            print("\nNo Matching Artefacts Found")

    input("\nPress Enter to return to the menu...")


def exit_program():
    """Exits the artefact management system."""

    print("\nExiting System. Have a Great Day!")

    time.sleep(2)

    sys.exit()
    clear_screen()

    print("\n--- Delete Artefact ---")

    search_name = input("Enter artefact name to delete: ").strip()

    artefact_found = False
    record_position = -1

    for i in range(len(artefact_list)):

        if artefact_list[i][0].lower() == search_name.lower():

            artefact_found = True
            record_position = i

            break

    if artefact_found:

        confirmation = input(
            "Are you sure you want to delete this artefact? (Yes/No): "
        ).strip()

        if confirmation.lower() == "yes":

            del artefact_list[record_position]



def main():
    """Main function to run the artefact management system."""

    while True:

        clear_screen()

        display_menu()

        choice = input("Enter your choice (1-10): ").strip()

        if choice == '1':
            add_artefact()

        elif choice == '2':
            update_condition()

        elif choice == '3':
            view_artefacts()

        elif choice == '4':
            search_artefact()

        elif choice == '5':
            delete_artefact()

        elif choice == '6':
            update_artefact_details()

        elif choice == '7':
            count_artefacts()

        elif choice == '8':
            filter_by_category()

        elif choice == '9':
            filter_by_condition()

        elif choice == '10':
            exit_program()

        else:
            print("\nInvalid Choice. Please Select 1 to 10.")
            time.sleep(2)


# Run the artefact management system

if __name__ == "__main__":
    main()
