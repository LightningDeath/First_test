def find_rec_index(index, n_dict):
    try:
        a = {index: [n_dict[str(index)][0]]}
    except KeyError:
        return 0
    return a
