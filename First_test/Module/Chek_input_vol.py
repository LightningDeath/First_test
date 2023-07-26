def ch_num_i(vol, st):
    # рекурсия для проверки правильности ввода числа
    try:
        v = int(vol)
    except ValueError:
        print('Вы ввели не число! Попробуйте еще раз!')
        return ch_num_i(input(f'Введите {st}: '), st)
    return int(v)


def ch_num_f(vol, st):
    # рекурсия для проверки правильности ввода числа
    try:
        v = float(vol)
    except ValueError:
        print('Вы ввели не число! Попробуйте еще раз!')
        return ch_num_f(input(f'Введите {st}: '), st)
    return float(v)


def ch_str(vol_1, st):
    try:
        if vol_1.isdigit() or vol_1 == '':
            print('Вы ввели не текст! Попробуйте еще раз!')
            return ch_str(input(f'Введите {st}: '), st)
        else:
            return vol_1
    except ValueError:
        print('Вы ввели не текст! Попробуйте еще раз!')
        return ch_str(input(f'Введите {st}: '), st)


def ch_sign(vol_1):
    sign_list = ['*', '/', '+', '-']
    if vol_1 in sign_list:
        return vol_1
    else:
        print('Вы ввели не верны знак операции! Попробуйте ещё!')
        return ch_sign(input('Введите вид операции: '))
