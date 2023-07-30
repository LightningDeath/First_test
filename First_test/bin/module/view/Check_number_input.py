def ch_num_i(vol, st):
    # рекурсия для проверки правильности ввода числа
    try:
        v = int(vol)
    except ValueError:
        print('Вы ввели не число! Попробуйте еще раз!')
        return ch_num_i(input(f'{st}'), st)
    return int(v)
