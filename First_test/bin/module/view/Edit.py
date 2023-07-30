def edit(ch, index, n_dict):
    if ch == 2:
        print("\nВведите новый заголовок")
        return input("--> ")
    else:
        print(f"\nТекущая запись:\n{n_dict[index][0]['text']}")
        print("Введите новую запись, либо скопируйте и вставьте старую и внесите необходимые изменения")
        return input("--> ")