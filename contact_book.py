def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact {name} added.")

def search_contact(name):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("SORRY, contact not found.")

def display_contacts():
    if contacts:
        for name, phone in contacts.items():
            print(f"{name} → {phone}")
    else:
        print("SORRY, no contacts saved yet.")

contacts = {}
while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Show All Contacts")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        add_contact(name, phone)
    elif choice == "2":
        name = input("Enter name to search: ")
        search_contact(name)
    elif choice == "3":
        display_contacts()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
