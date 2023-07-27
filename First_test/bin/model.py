import datetime
import json
import os

path = os.getcwd() + r"\data\note.json"


def add_note(note_list, index, n_dict):
    now = datetime.datetime.now()
    if index == 1:
        note_dict = {index: [
            {
                'date': now.strftime("%d-%m-%Y %H:%M"),
                'header': note_list[0],
                'text': note_list[1],
                'Modified': now.strftime("%d-%m-%Y %H:%M")
            }
        ]
        }
        with open(path, 'w') as t:
            t.write(json.dumps(note_dict, indent=4, ensure_ascii=False))
    else:
        note_dict = {index: [
            {
                'date': now.strftime("%d-%m-%Y %H:%M"),
                'header': note_list[0],
                'text': note_list[1],
                'Modified': now.strftime("%d-%m-%Y %H:%M")
            }
        ]
        }
        n_dict.update(note_dict)
        with open(path, 'w') as t:
            t.write(json.dumps(n_dict, indent=4, ensure_ascii=False))


def find_rec_index(index, n_dict):
    a = n_dict[str(index)][0]
    return a


def find_rec_date(date):
    pass


def find_rec_header(header):
    pass


def find_rec_modified(date_mod):
    pass


def delete_rec():
    pass


def read_note():
    pass


def clear_note():
    with open(path, 'w'):
        pass


def edit_note():
    pass
