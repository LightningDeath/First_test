def edit_note(flag, index, text, note_dict):
    """ Функция изменяет текст или заголовок по индексу"""
    if flag == 1:
        note_dict[index][0]["text"] = text
    else:
        note_dict[index][0]["header"] = text
    return note_dict
