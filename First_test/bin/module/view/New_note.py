def new_note():
    header = input("\nВведите заголовок заметки: ")
    print("Введите текст заметки:")
    text = input()
    note_list = (header, text)
    return note_list
