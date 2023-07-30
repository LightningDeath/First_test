from bin.module.view.Check_number_input import ch_num_i


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
