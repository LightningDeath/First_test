import json
import datetime


def add_note(path, note_list, index, n_dict):
    now = datetime.datetime.now()
    note_dict = {index: [
        {
            'date': now.strftime("%d.%m.%Y %H:%M"),
            'header': note_list[0],
            'text': note_list[1],
            'modified': now.strftime("%d.%m.%Y %H:%M")
        }
    ]
    }
    n_dict.update(note_dict)
    with open(path, 'w') as t:
        t.write(json.dumps(n_dict, indent=4, ensure_ascii=False))
