import json


def open_file(path):
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
