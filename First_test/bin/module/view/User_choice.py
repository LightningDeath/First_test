from bin.module.view.Check_number_input import ch_num_i


def user_choice():
    print("\nВыберите действие:\n"
          "1 - Добавить запись;\n"
          "2 - Найти запись;\n"
          "3 - Удалить запись;\n"
          "4 - Вывести на экран все записи;\n"
          "5 - Очистить записную книжку;\n"
          "6 - Редактировать запись;\n"
          "7 - Выход из программы.")
    choice = ch_num_i(input("\nВведите Ваш выбор: "), "Введите Ваш выбор: ")
    if choice > 7 or choice < 1:
        print("\nНе верный параметр! Повторите ввод.")
        return user_choice()
    return choice