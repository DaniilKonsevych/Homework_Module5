def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Please input the contact's name (and it's phone number if you are adding/changing one)."
        except IndexError:
            return "No data was inputed when required."
        except KeyError:
            return "The contact already exists/doesn't exist yet."
    return inner

@input_error
def add_contact(args, contacts):
        if args[0] not in contacts.keys():
            name, phone = args
            contacts[name] = phone
            return "Contact added."
        else:
            return "Contact already exists - can't add."

@input_error
def change_contact(args, contacts):
        if args[0] in contacts.keys():
            name, phone = args
            contacts[name] = phone
            return "Contact changed."
        else:
            return "Contact doesn't exist yet - can't change."

@input_error
def phone(args, contacts):
    return contacts[args[0]]

def main():
    contacts = {}
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
        elif command == "all":
            print(contacts)
        elif command == "phone":
            print(phone(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()