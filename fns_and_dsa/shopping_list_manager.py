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
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item")
            shopping_list.append(item) # Prompt for and add an item
            print("Item added")
            pass
        elif choice == '2':
            item = input("Enter the item") # Prompt for and remove an item
            if item in shopping_list:
                shopping_list.remove(item)
                print("Item removed")
            else:
                print("Item cannot be found.")
            pass
        elif choice == '3':
            print("Your shopping list:", shopping_list)  # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()