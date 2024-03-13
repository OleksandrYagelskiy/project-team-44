"""Module providing a function printing bot messages."""
from console_bot.input_manager import InputManager

def print_help():
    """Function printing help messagefor bot."""
    help_text = """
Available commands:
  hello                          - Ask the bot how it can help you.
  add [name] [phone]             - Adds a contact with the specified name and phone number.
  change [name] [phone]          - Changes the phone number for the specified contact.
  phone [name]                   - Retrieves the phone number for the specified contact.
  all                            - Displays all contacts in the system.
  help                           - Shows this help message.
  add-birthday [name] [birthday] - Adds birthday to the contact
  show-birthday [name]           - Shows birthday for specific contact
  birthdays                      - Shows birthdays for all contacts celebrating next week
  add-note                       - Adds note to Note Book.
  find-notes                     - Search notes by keywords.
  delete-note                    - Delete note by index in Note Book.
  edit-note                      - Edit note by index in Note Book.
  all-notes                      - Show all notes in Note Book.
  close/exit                     - Exits the program.
  save                           - Store current book to json file with name result.json
  restore                        - Restore book from result.json
  random-book                    - generate random book with 10 contacts
"""
    print(help_text)



def main():
    """Central function printing all the commands"""
    input_manager = InputManager()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = input_manager.parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(input_manager.add_contact(args))
        elif command == "change":
            print(input_manager.change_contact(args))
        elif command == "phone":
            print(input_manager.get_contact_phone(args))
        elif command == "all":
            print(input_manager.get_all_contacts())
        elif command == "help":
            print_help()
        elif command == "add-birthday":
            print(input_manager.add_birthday(args))
        elif command == "show-birthday":
            print(input_manager.show_birthday(args))
        elif command == "birthdays":
            print(input_manager.get_next_week_birthdays())
        elif command == "random-book":
            print(input_manager.generate_random_book())
        elif command == "add-note":
            note = input("Enter your note: ")
            print(input_manager.add_note(note))
        elif command == "find-notes":
            keyword = input("Enter searching keyword: ")
            print(input_manager.find_notes(keyword))
        elif command == "delete-note":
            # TODO: add option to delete by name
            index = input("Enter index of note you want to remove: ")
            print(input_manager.delete_note(index))
        elif command == "edit-note":
            index = input("Enter index of note you want to change: ")
            new_note = input("Enter a new note: ")
            print(input_manager.edit_note(index, new_note))
        elif command == "all-notes":
            print(input_manager.all_notes())
        elif command == "save":
            print(input_manager.save_to_json())
        elif command == "restore":
            print(input_manager.load_from_json())
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
