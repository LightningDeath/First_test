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
