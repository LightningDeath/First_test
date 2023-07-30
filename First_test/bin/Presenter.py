import time

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

    elif choice == 2:  # поиск записи

        # проверка, пустой ли файл
        if open_file[0] == 1:
            v.info("\nЗаписей нет.")
            if v.repeat() == 1:
                run()
            else:
                v.info("\nВсего наилучшего!")
                exit(0)

        # Поиск записи по выбранному пользователем критерию поиска
        c = v.find_or_delete_record("поиска")
        if c == 1:  # по номеру записи
            record = m.find_rec_index(v.enter_index(), open_file[1])
            if record == 0:
                v.info("\nЗаписи с таким номером не найдено.")
                if v.repeat() == 1:
                    run()
                else:
                    v.info("\nВсего наилучшего!")
                    exit(0)
        elif c == 2:
            record = m.find_rec_header(v.enter_header(), open_file[1])
            if len(record) == 0:
                v.info("\nЗаписи с таким заголовком не найдено.")
                if v.repeat() == 1:
                    run()
                else:
                    v.info("\nВсего наилучшего!")
                    exit(0)
        elif c == 3:
            record = m.find_rec_date(v.enter_date("добавления"), "date", open_file[1])
            if len(record) == 0:
                v.info("\nЗаписи с такой датой добавления не найдено.")
                if v.repeat() == 1:
                    run()
                else:
                    v.info("\nВсего наилучшего!")
                    exit(0)
        elif c == 4:
            record = m.find_rec_date(v.enter_date("изменения"), "modified", open_file[1])
            if len(record) == 0:
                v.info("\nЗаписи с такой датой изменения не найдено.")
                if v.repeat() == 1:
                    run()
                else:
                    v.info("\nВсего наилучшего!")
                    exit(0)
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

    elif choice == 4:  # вывод на экран всех записей
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

    elif choice == 5:  # очистка записной книжки
        v.info("Вы уверены, что хотите удалить все записи?")
        if v.warning() == 1:
            m.clear_note()
            v.info("\nОчистка записной книги завершена.")

    elif choice == 6:  # редактирование записи
        if m.check_empty(open_file[1]) == 100:
            v.info("\nЗаписей для редактирования нет.")
        else:
            n = 0
            param = v.get_parameter("номер", "доступных", open_file[1])
            if param == 0:
                v.view_result(open_file[1])
                k = 0
                while n == 0:
                    f = v.get_parameter("номер", "доступных", open_file[1])
                    if f == 0:
                        v.view_result(open_file[1])
                        if v.repeat_message(k) == 1:
                            time.sleep(5)
                            run()
                    else:
                        param = f
                        n = 1
                    k += 1
            f_dict = m.find_rec_index(str(param), open_file[1])
            if f_dict == 0:
                v.info("\nЗаписи с таким номером не найдено!")
            else:
                b = v.wath_edit()
                if b == 1:  # редактирование по индексу
                    new_text = v.edit(b, str(param), f_dict)
                    new_dict = m.edit_note(b, str(param), new_text, open_file[1])
                    m.rewrite(new_dict)
                    v.info("\nЗапись успешно отредактирована.")
                else:  # редактирование по заголовку
                    new_text = v.edit(b, str(param), f_dict)
                    new_dict = m.edit_note(b, str(param), new_text, open_file[1])
                    m.rewrite(new_dict)
                    v.info("\nЗапись успешно отредактирована.")

    elif choice == 7:  # выход из программы
        v.info("\nВсего наилучшего!")
        exit(0)

    # запрос на перезапуск или выход из программы
    if v.repeat() == 1:
        run()
    else:
        v.info("\nВсего наилучшего!")
        exit(0)
