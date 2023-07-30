import json


def rewrite(path, n_dict):
    with open(path, 'w') as t:
        t.write(json.dumps(n_dict, indent=4, ensure_ascii=False))