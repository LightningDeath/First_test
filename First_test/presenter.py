from re import match

import model
import view


def run():
    choice = view.user_choice()
    if choice == "1":
        note_list = view.new_note()
        print(note_list)
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        exit(0)
