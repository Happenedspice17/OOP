import os

def clear_console() -> None:
    os_name = os.name
    if os_name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def main_menu() -> None:
    print("Contact Book")
    print("0.- Save a contact")
    print("1.- Update a contact")
    print("2.- Delete a contact")
    print("3.- List all contacts")
    print("4.- Exit")

def login_multiple() -> None:
    all_contacts = {}
    contact_counter = 0
    
    program_running = True

    while program_running:
        clear_console()
        main_menu()
        user_option = int(input("Option: "))
        if user_option == 0:
            all_contacts, contact_counter = save_contact(all_contacts, contact_counter)
        elif user_option == 1:
            all_contacts = update_contact(all_contacts)
        elif user_option == 2:
            all_contacts, contact_counter = delete_contact(all_contacts, contact_counter)
        elif user_option == 3:
            list_contacts(all_contacts, contact_counter)
        elif user_option == 4:
            program_running = False
            print("Closing the program... Bye!")
        else:
            input("Option not valid... Press enter to continue...")

def save_contact(contacts, counter) -> tuple:
    clear_console()
    print("Add contacts")
    contn = input("Input the name of contact: ")
    contp = input("Input the phone number: ")
    conte = input("Input the email address: ")

    new_dict = {
        'phone': contp,
        'email': conte
    }

    if contn not in contacts:
        contacts[contn] = new_dict
        counter += 1
    else:
        input("The contact is already in the book. Press enter to continue...")

    return contacts, counter

def delete_contact(contacts, counter) -> tuple:
    clear_console()
    print("Delete contact")
    contn = input("Input the contact to delete: ")
    
    if contn in contacts:
        del contacts[contn]
        counter -= 1
        input("Contact deleted. Press enter to continue...")
    else:
        input("Contact not found. Press enter to continue...")

    return contacts, counter

def list_contacts(contacts, counter) -> None:
    clear_console()

    if counter == 0:
        input("The contact book is empty. Press enter to continue...")
    else:
        print("Display contacts:")
        for outer_key, inner_dict in contacts.items():
            print(f"Contact name: {outer_key}")
            for inner_key, value in inner_dict.items():
                print(f"\t{inner_key}: {value}")
                
def update_contact(contacts) -> tuple:
    
    user_menu_running = True
    while user_menu_running:
        clear_console()
        print("Edit contact book")
        print("1.- Edit contact by name")
        print("2.- Return to the main menu")
        user_option = int(input("Option: "))
        if user_option == 1:
            contacts = edit_contact(contacts)
        elif user_option == 2:
            user_menu_running = False
            input("Returning to the main menu... Press enter to continue...")
        else:
            input("Option not valid... Press enter to continue...")
    return contacts

def edit_contact(contacts) -> tuple:
    print()
    contn = input("Input the contact to edit: ")

    cont_in_book = contn in contacts

    if cont_in_book == True:
        contp = input("Input the new phone number: ")
        conte = input("Input the new email address: ")
        contacts[contn]['phone'] = contp
        contacts[contn]['email'] = conte
    else:
        input("The contact is not in the book. Press enter to continue...")

    return contacts

login_multiple()