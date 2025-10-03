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
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item = input("Enter item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f'"{item}" added.')
            else:
                print("No item entered.")
        elif choice == '2':
            item = input("Enter item to remove: ").strip()
            try:
                shopping_list.remove(item)
                print(f'"{item}" removed.')
            except ValueError:
                print("Item not found in the list.")
        elif choice == '3':
            if shopping_list:
                print("Current list:")
                for i, it in enumerate(shopping_list, 1):
                    print(f"{i}. {it}")
            else:
                print("The shopping list is empty.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
