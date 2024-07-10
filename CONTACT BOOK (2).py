# Contact Management System

contacts = {}
contact_id_counter = 3  # To generate new unique IDs for contacts

def add_contact(name, phone, email, address):
    global contact_id_counter
    contacts[contact_id_counter] = {"name": name, "phone": phone, "email": email, "address": address}
    contact_id_counter += 1
    print("Contact added successfully.")

def view_contacts():
    print("\nContact List:")
    for contact_id, contact_info in contacts.items():
        print(f"ID: {contact_id}, Name: {contact_info['name']}, Phone: {contact_info['phone']}, Email: {contact_info['email']}, Address: {contact_info['address']}")

def search_contact(query):
    results = []
    for contact_id, contact_info in contacts.items():
        if query.lower() in contact_info['name'].lower() or query in contact_info['phone']:
            results.append((contact_id, contact_info))
    return results

def update_contact(contact_id, name=None, phone=None, email=None, address=None):
    if contact_id in contacts:
        if name:
            contacts[contact_id]['name'] = name
        if phone:
            contacts[contact_id]['phone'] = phone
        if email:
            contacts[contact_id]['email'] = email
        if address:
            contacts[contact_id]['address'] = address
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact(contact_id):
    if contact_id in contacts:
        del contacts[contact_id]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Management System")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            view_contacts()
        elif choice == '2':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(name, phone, email, address)
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            results = search_contact(query)
            if results:
                print("Search Results:")
                for contact_id, contact_info in results:
                    print(f"ID: {contact_id}, Name: {contact_info['name']}, Phone: {contact_info['phone']}, Email: {contact_info['email']}, Address: {contact_info['address']}")
            else:
                print("No contacts found.")
        elif choice == '4':
            contact_id = int(input("Enter contact ID to update: "))
            update_choice = input("Update (N)ame, (P)hone, (E)mail, (A)ddress? ")
            if update_choice.upper() == 'N':
                new_name = input("Enter new name: ")
                update_contact(contact_id, name=new_name)
            elif update_choice.upper() == 'P':
                new_phone = input("Enter new phone number: ")
                update_contact(contact_id, phone=new_phone)
            elif update_choice.upper() == 'E':
                new_email = input("Enter new email: ")
                update_contact(contact_id, email=new_email)
            elif update_choice.upper() == 'A':
                new_address = input("Enter new address: ")
                update_contact(contact_id, address=new_address)
            else:
                print("Invalid update option.")
        elif choice == '5':
            contact_id = int(input("Enter contact ID to delete: "))
            delete_contact(contact_id)
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
