def display_menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")

def add_contact(contact_book):
    name = input("Contact name: ")

    if name in contact_book:
        print("Contact already exists!")
        return
    
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Home Address: ")
    
    contact_book[name] = {"phone": phone,
                          "email": email,
                          "address": address
                          }
    print("Contact added successfully!")

def view_contact(contact_book):
    name = input("Contact Name: ")
    if name in contact_book:
        contact = contact_book[name]
        print(f"Name: {name}")
        print(f"Phone: {contact_book[name]['phone']}")
        print(f"Email: {contact_book[name]['email']}")
        print(f"Address: {contact_book[name]['address']}")
    else:
        print("Contact not found!")

def edit_contact(contact_book):
    name = input("Contact Name: ")

    if name in contact_book:
        phone = input("Phone: ")
        email = input("Email: ")
        address = input("Address: ")

        if len(phone) < 10:
            print("Invalid phone number! Please enter a valid 10-digit phone number.")
            return
        if phone == "":
            phone = contact_book[name]['phone']
        if email == "":
            email = contact_book[name]['email']
        if address == "":
            address = contact_book[name]['address']

        contact_book[name] = {"phone": phone,
                              "email": email,
                              "address": address
                              }
    else:
        print("Contact not found!")

def delete_contact(contact_book):
    name = input("Name: ")

    if name in contact_book:
        del contact_book[name]
    else:
        print("Contact not found!")

def list_contacts(contact_book):
    if not contact_book:
        print("No Contacts available!")
    else:
        for name, details in contact_book.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print()

contact_book = {}

while True:
    display_menu()

    choice = input("Enter choice(1-6): ")

    if choice == "6":
        print("Exiting Application...GoodBye!")
        break
    elif choice == "1":
        add_contact(contact_book)
    elif choice == "2":
        view_contact(contact_book)
    elif choice == "3":
        edit_contact(contact_book)
    elif choice == "4":
        delete_contact(contact_book)
    elif choice == "5":
        list_contacts(contact_book)
    else:
        print("Invalid input!")