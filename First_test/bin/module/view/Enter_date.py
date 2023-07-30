import time


def enter_date(word):
    date = input(f'\nВведите дату {word} записи в формате ДД.ММ.ГГГГ: ')
    try:
        time.strptime(date, '%d.%m.%Y')
    except ValueError:
        print("\nДата введена не корректно! Попробуйте снова.")
        return enter_date(word)
    return date
