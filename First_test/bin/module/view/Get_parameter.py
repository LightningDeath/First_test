def get_parameter(text, text2, n_dict):
    print(f"\nВведите {text} записи, которую желаете отредактировать.\n Для просмотра {text2} записей введите '0'.")
    param = input("--> ")
    if param.isdigit():
        return int(param)
    else:
        print("Введено не число! Попробуйте ещё.")
        return get_parameter(text, text2, n_dict)
