def wath_edit():
    print("\nЧто будем редактировать?\n"
          "1 - Текст записи;\n"
          "2 - Заголовок.")
    a = input("--> ")
    if a.isdigit():
        if 1 > int(a) > 2:
            print("Введен не верный параметр! Попробуйте еще.")
            return wath_edit()
        return int(a)
    else:
        print("Введен не верный параметр! Попробуйте еще.")
        return wath_edit()
