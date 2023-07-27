import json
import os

from bin import model
from bin import view


def run():
    path = os.getcwd() + r"\data\note.json"
    try:
        with open(path) as n_d:
            n_dict = json.load(n_d)
            print(n_dict)
            index = list(list(list(n_dict)[-1])[-1])[-1]
            print(index)
            index = int(index) + 1
    except json.JSONDecodeError:
        n_dict = {}
        index = 1

    choice = view.user_choice()
    if choice == 1:
        note_list = view.new_note()
        if index == 1:
            model.add_note(note_list, index, n_dict)
        else:
            model.add_note(note_list, index, n_dict)
    elif choice == 2:
        if index == 1:
            ch = view.empty_note()
            if ch == 2:
                exit(0)
            elif ch == 1:
                run()
        c = view.find_or_delete_record("поиска")
        flag = 0

        if c == 1:
            note_index = view.enter_index()
            record = model.find_rec_index(note_index, n_dict)
            view.view_result(flag, note_index, record)
        elif c == 2:
            model.find_rec_header(view.enter_header())
        elif c == 3:
            model.find_rec_date(view.enter_date())
        elif c == 4:
            model.find_rec_modified(view.enter_modified())

    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        model.clear_note()
    elif choice == 6:
        exit(0)
