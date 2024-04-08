# Hierancy

class ContactInfo():

    def __init__(self) -> None:
        self.name = ""
        self.email = ""
        self.phone = ""
        self.add_contact()

    def add_contact(contact_book):
        name = input("Enter contact name: ")
        if name in contact_book:
            print("Contact already exists.")
        else:
            self.name = input("Enter phone number: ")
            email = input("Enter email address: ")
            contact_book[name] = {"phone": phone, "email": email}
            print("Contact added successfully.")

    def update_contact(contact_book):
        name = input("Enter the name of the contact to update: ")
        if name not in contact_book:
            print("Contact not found.")
        else:
            phone = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            contact_book[name] = {"phone": phone, "email": email}
            print("Contact updated successfully.")

    def delete_contact(contact_book):
        name = input("Enter the name of the contact to delete: ")
        if name in contact_book:
            del contact_book[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")



class ContactBook():

    def __init__(self) -> None:
        pass


    def list_contacts(contact_book):
        if not contact_book:
            print("The contact book is empty.")
        else:
            for name, details in contact_book.items():
                print(f"\nContact Name: {name}")
                print(f"Phone Number: {details['phone']}")
                print(f"Email: {details['email']}")