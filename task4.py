def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact changed"


def return_phone(args, contacts):
    username = args[0]
    return contacts[username]


def main():
    contacts = {"Maksym": "0682082130"}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

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
            print(return_phone(args, contacts))
        elif command == "all":
            try:
                max_key_length = max(len(str(key)) for key in contacts)
                for key, value in contacts.items():
                    print(f"{str(key):<{max_key_length}} : {value}")
            except ValueError:
                print("No contacts found")
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
