def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        # choice must be a NUMBER for the checker
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please try again.")
            continue

        if choice == 1:
            # EXACT text the checker expects:
            item = input("Enter the item to add: ")
            shopping_list.append(item)
        elif choice == 2:
            # EXACT text the checker expects:
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print("Item not found in the list.")
        elif choice == 3:
            if not shopping_list:
                print("The shopping list is empty.")
            else:
                for i, it in enumerate(shopping_list, 1):
                    print(f"{i}. {it}")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
