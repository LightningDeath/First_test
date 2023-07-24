from Module import Chek_input_vol


def user_choice():
    print("\nВыберите действие:\n"
          "1 - Добавить запись;\n"
          "2 - Найти запись;\n"
          "3 - Удалить запись;\n"
          "4 - Вывести на экран все записи;\n"
          "5 - Очистить записную книжку;\n"
          "6 - Выход из программы.")
    print("Ваш выбор:")
    choice = input()
    return choice


def new_note():
    print("Введите заголовок заметки:")
    header = input()
    print("Введите текст заметки:")
    text = input()
    note_list = (header, text)
    return note_list
