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

        choice = input("Enter your choice (1-4): ").strip()

        if not choice.isdigit():
            print("Please enter a number (1-4).")
            continue

        choice = int(choice)

        if choice == 1:
            item = input("Enter item to add: ").strip()
            shopping_list.append(item)
            print(f"'{item}' added to the list.")

        elif choice == 2:
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from the list.")
            else:
                print(f"'{item}' not found in the shopping list.")

        elif choice == 3:
            if shopping_list:
                print("Current Shopping List:")
                index = 1
                for item in shopping_list:
                    print(f"{index}. {item}")
                index += 1
            else:
                print("Your shopping list is currently empty.")

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 4.")

if __name__ == "__main__":
    main()
