import menu

contact_book = menu.ContactBook()
while True:
    contact_book.display_menu()
    choice = input("Enter your choice: ")
    try:
        choice = int(choice)
    except ValueError:
        print("Invalid choice! Please enter a number.")
        continue
    if choice == 1:
        print("")
        contact_book.add_contact()
    elif choice == 2:
        print("")
        contact_book.view_contact()
    elif choice == 3:
        print("")
        contact_book.edit_contact()
    elif choice == 4:
        print("")
        contact_book.delete_contact()
    elif choice == 5:
        print("")
        contact_book.list_all_contacts()
    elif choice == 6:
        print("Exiting the book...")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
