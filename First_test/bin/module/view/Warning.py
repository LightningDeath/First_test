from bin.module.view.Check_number_input import ch_num_i


def warning():
    print("1 - да;\n"
          "2 - нет.")
    a = ch_num_i(input(), "1 - да;\n2 - нет.")
    if a < 1 or a > 2:
        print("Введен не корректный параметр!попробуйте ещё.")
        return warning()
    return a
