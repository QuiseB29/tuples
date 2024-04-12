def display_contacts(contacts):
    print("\nContacts:")
    for contact in contacts:
        name,email,phone = contact
        print(f"Name:{name}, Email:{email}, Phone: {phone}")


contacts = [
    ("Alice", "alice@email.com", "123-456-7890"),
    ("Bob", "bob@email.com", "234-567-8901"),
    ("Zane", "zmoney@email.com", "314-334-2222"),
    ("Lance", "laneb23@email.com", "892-222-2123"),
]

display_contacts(contacts)