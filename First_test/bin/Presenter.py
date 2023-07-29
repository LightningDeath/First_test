from bin import Model as m
from bin import View as v


def run():
    global record, delete_param
    open_file = m.open_file()
    choice = v.user_choice()

    if choice == 1:
        # добавление записи
        note_list = v.new_note()
        m.add_note(note_list, open_file[0], open_file[1])
        v.info("\nДобавление выполнено!")

    elif choice == 2:
        # поиск записи
        if open_file[0] == 1:
            v.info("\nЗаписей нет.")
            if v.repeat() == 1:
                run()
            else:
                v.info("\nВсего наилучшего!")
                exit(0)
        c = v.find_or_delete_record("поиска")
        # Поиск записи по выбранному пользователем критерию поиска
        if c == 1:
            record = m.find_rec_index(v.enter_index(), open_file[1])
        elif c == 2:
            record = m.find_rec_header(v.enter_header(), open_file[1])
        elif c == 3:
            record = m.find_rec_date(v.enter_date("добавления"), "date", open_file[1])
        elif c == 4:
            record = m.find_rec_date(v.enter_date("изменения"), "modified", open_file[1])
        v.view_result(record)

    elif choice == 3:
        # Удаление записи по выбранному пользователем критерию
        c = v.find_or_delete_record("удаления")
        if c == 1:
            delete_param = v.enter_index()
        elif c == 2:
            delete_param = v.enter_header()
        elif c == 3:
            delete_param = v.enter_date("добавления")
        elif c == 4:
            delete_param = v.enter_date("изменения")
        new_note_dict = m.delete_rec(c, delete_param, open_file[1])
        if new_note_dict == 1:
            v.info("\nЗаписей для удаления не найдено.")
        else:
            m.rewrite(new_note_dict)
            v.info("\nУдаление завершено.")

    elif choice == 4:
        note = m.read_note()
        if note == 1:
            v.info("\nНет записей.")
            if v.repeat() == 1:
                run()
            else:
                v.info("\nВсего наилучшего!")
                exit(0)
        else:
            v.view_result(note)
    elif choice == 5:
        m.clear_note()
        v.info("\nОчистка записной книги завершена.")

    elif choice == 6:
        v.info("\nВсего наилучшего!")
        exit(0)

    if v.repeat() == 1:
        run()
    else:
        v.info("\nВсего наилучшего!")
        exit(0)
