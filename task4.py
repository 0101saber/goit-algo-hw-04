def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def is_contact(name, contacts) -> bool:
    if contacts.get(name):
        return True
    else:
        return False


def find_contact(args, contacts):
    name = args
    if is_contact(name, contacts):
        return contacts[name]
    else:
        return 'Contact name not found.'


def change_contact(args, contacts):
    name, phone = args
    if is_contact(name, contacts):
        contacts[name] = phone
        return "Contact change."
    return 'Contact not change.'


def main():
    print("Welcome to the assistant bot!")
    contacts = {}
    while True:
        command, *args = parse_input(input("Enter a command: "))

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(find_contact(args[0], contacts))
        elif command == "all":
            print("Name   Phone")
            for name, phone in contacts.items():
                print(f'{name}: {phone}')
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
