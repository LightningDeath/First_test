from bin.module.view.Check_number_input import ch_num_i


def repeat():
    print("\nЖелаете продолжить?(1 - да, 2 - нет)")
    c = ch_num_i(input("Введите Ваш выбор: "), "Введите Ваш выбор: ")
    if c > 2 or c < 1:
        print("\nНе верный параметр! Повторите ввод.")
        return repeat()
    return c