import datetime
import json
import os

path = os.getcwd() + r"\data\note.json"


def open_file():
    try:
        with open(path) as n_d:
            n_dict = json.load(n_d)
            index = list(list(list(n_dict)[-1])[-1])[-1]
            index = int(index) + 1
    except json.JSONDecodeError:
        n_dict = {}
        index = 1
    result = [index, n_dict]
    return result


def add_note(note_list, index, n_dict):
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


def find_rec_index(index, n_dict):
    a = {index: [n_dict[str(index)][0]]}
    return a


def find_rec_header(header, n_dict):
    new_note_dict = {}
    for i in n_dict:
        if n_dict[i][0]["header"] == header:
            new_note_dict.update({i: [n_dict[i][0]]})
    return new_note_dict


def find_rec_date(date, word, n_dict):
    find_dict = {}
    for i in n_dict:
        date_record = n_dict[i][0][word]
        date_record = date_record.split(" ")
        if date == date_record[0]:
            find_dict.update({i: [n_dict[i][0]]})
    return find_dict


def delete_rec(flag, value, n_dict):
    new_dict = {}
    n = 1
    if flag == 1:
        for i in n_dict:
            if n == 1:
                if i != str(value):
                    new_dict.update({n: [n_dict[i][0]]})
                    n += 1
            else:
                if i != str(value):
                    new_dict.update({n: [n_dict[i][0]]})
                    n += 1

    elif flag == 2:
        for i in n_dict:
            if n == 1:
                if n_dict[i][0]["header"] != value:
                    new_dict.update({n: [n_dict[i][0]]})
                    n += 1
            else:
                if n_dict[i][0]["header"] != value:
                    new_dict.update({n: [n_dict[i][0]]})
                    n += 1

    elif flag == 3:
        for i in n_dict:
            date = n_dict[i][0]["date"]
            date = date.split(" ")
            if n == 1:
                if date[0] != value:
                    new_dict.update({n: [n_dict[i][0]]})
                    n += 1
            else:
                if date[0] != value:
                    new_dict.update({n: [n_dict[i][0]]})
                    n += 1

    elif flag == 4:
        for i in n_dict:
            date = n_dict[i][0]["modified"]
            date = date.split(" ")
            if n == 1:
                if date[0] != value:
                    new_dict.update({n: [n_dict[i][0]]})
                    n += 1
            else:
                if date[0] != value:
                    new_dict.update({n: [n_dict[i][0]]})
                    n += 1

    if len(new_dict) == len(n_dict):
        return 1
    return new_dict


def read_note():
    try:
        with open(path) as n_d:  # если не пустой, то получаем данные
            n_dict = json.load(n_d)
    except json.JSONDecodeError:  # если пустой выдаем флаг, обозначающий, что файл пустой
        return 1
    return n_dict


def clear_note():
    with open(path, 'w'):
        pass


def edit_note():
    pass


def rewrite(n_dict):
    with open(path, 'w') as t:
        t.write(json.dumps(n_dict, indent=4, ensure_ascii=False))
