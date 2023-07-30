def find_rec_header(header, n_dict):
    new_note_dict = {}
    for i in n_dict:
        if n_dict[i][0]["header"] == header:
            new_note_dict.update({i: [n_dict[i][0]]})
    return new_note_dict
