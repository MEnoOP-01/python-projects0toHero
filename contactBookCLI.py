/*
## Contact Book CLI
A command line contact book built with python
1. Add, view, search and delete contacts
2. Input validation on name, phone and email
3. Run with: python contact_book.py
*/




# Add contacts list
def add_details(contactBook: list) -> None:
    # pass
    # Enter name  : Aryan
    n = str(input("Enter name: ")).strip()
    if not n.isalpha():
        print("Invalid name")
        return

    # Enter phone : 9876543210
    phno = str(input("Enter phone: ")).strip()
    if not phno.isdigit() or len(phno)!=10:
        print("Invalid phone! Must be 10 digits.")
        return


    # Enter email : aryan@gmail.com
    e = input("Enter email: ").strip().lower()
    if not '@' in e:
        print("Invalid email!")
        return

    contactBook.append({"name": n.title(), "phone": phno, "email": e})
    print("Contact added successfully!")
    # message: successful

# view all the stored contacts
def view(contactBook: list) -> None:
    # pass
    if not contactBook:
        print('No contacts yet saved')
        return

    print('-'*6, "All contacts", '-'*6)
    for i, c in enumerate(contactBook, 1):
        print(f"{i}. {c.get('name')} | {c.get('phone')} | {c.get('email')}")


# search the contact
def search(contactBook: list) -> None:
    # pass
    user_input = str(input('Enter name to search: ')).strip().lower()
    for k in contactBook:
        if k.get("name").lower() == user_input:
            print(f"Found: {k.get('name')} | {k.get('phone')} | {k.get('email')}")
            return
    print("contact not found!")


def remove_contact(contactBook: list) -> None:
    # pass
    user_input = str(input('Enter name to delete: ')).strip().lower()
    for k in contactBook:
        if k.get("name").lower() == user_input:
            contactBook.remove(k)
            print("Contact deleted successfully!")
            return
    print("Contact not found!")



# contact book menu
contactBook=[]

while True:
    try:
        print('='*30,'\n',' '*6,'CONTACT BOOK\n','='*30)
        print('''1. Add contact \n2. View all contacts \n3. Search contact \n4. Delete contact \n5. Quit\n''', '='*30)
        # wait for user reference
        n = int(input('Choose an option (1-5):'))
        match n:
            case 1: add_details(contactBook)
            case 2: view(contactBook)
            case 3: search(contactBook)
            case 4: remove_contact(contactBook)
            case 5: break
            case _: 
                    print("Choose from the given options")
                    continue

    except ValueError:
        print("That was not a valid number!")
