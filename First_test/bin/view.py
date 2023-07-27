def user_choice():
    print("\nВыберите действие:\n"
          "1 - Добавить запись;\n"
          "2 - Найти запись;\n"
          "3 - Удалить запись;\n"
          "4 - Вывести на экран все записи;\n"
          "5 - Очистить записную книжку;\n"
          "6 - Выход из программы.")
    choice = ch_num_i(input("\nВведите Ваш выбор: "), "Введите Ваш выбор: ")
    if choice > 6 or choice < 1:
        print("\nНе верный параметр! Повторите ввод.")
        return user_choice()
    return choice


def new_note():
    header = input("\nВведите заголовок заметки: ")
    print("Введите текст заметки:")
    text = input()
    note_list = (header, text)
    return note_list


def find_or_delete_record(value):
    print(f'Выберите критерий {value} записи:\n'
          f'1 - по номеру;\n'
          f'2 - по заголовку;\n'
          f'3 - по дате добавления;\n'
          f'4 - по дате изменения.\n')
    choice = ch_num_i(input("Введите Ваш выбор: "), "Введите Ваш выбор: ")
    if choice > 4 or choice < 1:
        print("Не верный параметр! Повторите ввод.")
        return find_or_delete_record(value)
    return choice


def enter_index():
    choice = ch_num_i(input("Введите номер записи: "), "Введите номер записи: ")
    return choice


def enter_header():
    choice = input("Введите заголовок записи: ")
    return choice


def enter_date():
    choice = input("Введите дату добавления записи: ")
    return choice


def enter_modified():
    choice = input("Введите дату изменения записи: ")
    return choice


def empty_note():
    print("\nЗаписей нет.\nЖелаете продолжить?(1 - да, 2 - нет)")
    c = ch_num_i(input("Введите Ваш выбор: "), "Введите Ваш выбор: ")
    if c > 2 or c < 1:
        print("\nНе верный параметр! Повторите ввод.")
        return empty_note()
    return int(c)


def view_result(flag, index, note_rec):
    if flag == 0:
        print(f'\nНомер записи:               {index}')
        print(f'Дата создания:              {note_rec["date"]}')
        print(f'Дата последней модификации: {note_rec["Modified"]}')
        print(f'Заголовок записи:           {note_rec["header"]}')
        print(f'Текст записи: \n '
              f'{note_rec["text"]}')
    else:
        for i in note_rec:
            print(f'\nНомер записи:               {i}')
            print(f'Дата создания:              {i["date"]}')
            print(f'Дата последней модификации: {note_rec["Modified"]}')
            print(f'Заголовок записи:           {note_rec["header"]}')
            print(f'Текст записи: \n '
                  f'{note_rec["text"]}')


def ch_num_i(vol, st):
    # рекурсия для проверки правильности ввода числа
    try:
        v = int(vol)
    except ValueError:
        print('Вы ввели не число! Попробуйте еще раз!')
        return ch_num_i(input(f'{st}'), st)
    return int(v)
