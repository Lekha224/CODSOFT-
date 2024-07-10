contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    print(f"Contact {name} added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    print("\nContact List:")
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

def search_contact():
    if not contacts:
        print("No contacts found.")
        return
    search_term = input("Enter name or phone to search: ")
    results = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
    if not results:
        print("No matching contacts found.")
        return
    print("\nSearch Results:")
    for contact in results:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

def update_contact():
    if not contacts:
        print("No contacts found to update.")
        return
    name = input("Enter name of the contact to update: ")
    found = False
    for contact in contacts:
        if contact['name'] == name:
            found = True
            contact['phone'] = input("Enter new phone (leave blank to keep current): ") or contact['phone']
            contact['email'] = input("Enter new email (leave blank to keep current): ") or contact['email']
            contact['address'] = input("Enter new address (leave blank to keep current): ") or contact['address']
            print(f"Contact {name} updated successfully.")
            break
    if not found:
        print(f"Contact {name} not found.")

def delete_contact():
    if not contacts:
        print("No contacts found to delete.")
        return
    name = input("Enter name of the contact to delete: ")
    contacts
    initial_length = len(contacts)
    contacts = [contact for contact in contacts if contact['name'] != name]
    if len(contacts) < initial_length:
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found.")

def main():
    while True:
        print("\nContact Manager Menu")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
