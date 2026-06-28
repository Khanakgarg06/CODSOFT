# Dictionary to store contacts
contacts = {}

# Add Contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }

    print("Contact Added Successfully!")

# View Contacts
def view_contacts():

    if not contacts:
        print("No Contacts Available.")

    else:
        print("\n===== CONTACT LIST =====")

        for name, details in contacts.items():
            print(f"Name : {name}")
            print(f"Phone : {details['phone']}")
            print("-" * 30)

# Search Contact
def search_contact():

    search = input("Enter Name or Phone Number: ")

    found = False

    for name, details in contacts.items():

        if search.lower() == name.lower() or search == details["phone"]:

            print("\n===== CONTACT FOUND =====")
            print("Name    :", name)
            print("Phone   :", details["phone"])
            print("Email   :", details["email"])
            print("Address :", details["address"])

            found = True

    if not found:
        print("Contact Not Found.")

# Update Contact
def update_contact():

    name = input("Enter Contact Name to Update: ")

    if name in contacts:

        contacts[name]["phone"] = input("Enter New Phone Number: ")
        contacts[name]["email"] = input("Enter New Email: ")
        contacts[name]["address"] = input("Enter New Address: ")

        print("Contact Updated Successfully!")

    else:
        print("Contact Not Found.")

# Delete Contact
def delete_contact():

    name = input("Enter Contact Name to Delete: ")

    if name in contacts:

        del contacts[name]

        print("Contact Deleted Successfully!")

    else:
        print("Contact Not Found.")

# Main Program
while True:

    print("\n==========================")
    print("     CONTACT BOOK")
    print("==========================")

    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Thank You for Using Contact Book!")
        break

    else:
        print("Invalid Choice! Please Try Again.")