import datetime
import json


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
        with open('../data/note.json', 'w') as t:
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
        n_dict[0].update(note_dict)
        with open('../data/note.json', 'w') as t:
            t.write(json.dumps(n_dict, indent=4, ensure_ascii=False))


def find_rec_index(index, n_dict):
    pass


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
    with open('../data/note.json', 'w'):
        pass


def edit_note():
    pass
