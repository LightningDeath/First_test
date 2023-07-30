def find_rec_date(date, word, n_dict):
    find_dict = {}
    for i in n_dict:
        date_record = n_dict[i][0][word]
        date_record = date_record.split(" ")
        if date == date_record[0]:
            find_dict.update({i: [n_dict[i][0]]})
    return find_dict
