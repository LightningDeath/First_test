import json


def read_note(path):
    try:
        with open(path) as n_d:  # если не пустой, то получаем данные
            n_dict = json.load(n_d)
    except json.JSONDecodeError:  # если пустой выдаем флаг, обозначающий, что файл пустой
        return 1
    return n_dict
