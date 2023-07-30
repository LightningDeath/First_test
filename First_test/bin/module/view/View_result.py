def view_result(note_rec):
    if len(note_rec) == 0:
        print("\nЗаписей нет.")
    else:
        for i in note_rec:
            print(f'\nНомер записи:               {i}')
            print(f'Дата создания:              {note_rec[i][0]["date"]}')
            print(f'Дата последней модификации: {note_rec[i][0]["modified"]}')
            print(f'Заголовок записи:           {note_rec[i][0]["header"]}')
            print(f'Текст записи: \n '
                  f'{note_rec[i][0]["text"]}')