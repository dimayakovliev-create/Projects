import colorama
colorama.init()


def parse_input(user_input):
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args
    except ValueError:
        return None, []

def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return f"{colorama.Fore.GREEN}Contact added.{colorama.Style.RESET_ALL}"
    except ValueError:
        return f"Invalid input format. Please provide: {colorama.Fore.BLUE}add{colorama.Style.RESET_ALL} name and phone number."

def change_contact(args, contacts):
    try:
        name, phone = args  
        if name in contacts:
            contacts[name] = phone
            return f"{colorama.Fore.GREEN}Contact updated.{colorama.Style.RESET_ALL}"
        else:
            return f"{colorama.Fore.YELLOW}Contact not found.{colorama.Style.RESET_ALL}"
    except ValueError:
        return f"Invalid input format. Please provide: {colorama.Fore.BLUE}change{colorama.Style.RESET_ALL} name and new phone number."

def phone_username(args, contacts):
    try:
        name = args[0]
        if name in contacts:
            return f"{colorama.Fore.GREEN}{name}'s phone number is {contacts[name]}.{colorama.Style.RESET_ALL}"
        else:
            return f"{colorama.Fore.YELLOW}Contact not found.{colorama.Style.RESET_ALL}"
    except IndexError:
        return f"Invalid input format. Please provide: {colorama.Fore.BLUE}phone{colorama.Style.RESET_ALL} name."


def all_contacts(contacts):
    if contacts:
        return "\n".join([f"{colorama.Fore.GREEN}{name}: {phone}{colorama.Style.RESET_ALL}" for name, phone in contacts.items()])
    else:
        return f"{colorama.Fore.RED}No contacts found!{colorama.Style.RESET_ALL}"

def main():
    contacts = {}
    print(f"{colorama.Fore.GREEN}Welcome to the assistant bot!{colorama.Style.RESET_ALL}")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(f"{colorama.Fore.YELLOW}Good bye!{colorama.Style.RESET_ALL}")
            break
        elif command == "hello":
            print(f"{colorama.Fore.YELLOW}Hello! How can I help you?{colorama.Style.RESET_ALL}")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(phone_username(args, contacts))
        elif command == "all":
            print(all_contacts(contacts))
        elif command == "":
            continue
        else:
            print(f"Invalid command. Available commands: {colorama.Fore.BLUE}hello, add, change, phone, all, exit, close{colorama.Style.RESET_ALL}")


if __name__ == "__main__":
    main()
