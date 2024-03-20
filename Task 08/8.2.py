FILE_NAME = 'phone1.txt'
ID = 'id'
LAST_NAME = 'фамилия'
FIRST_NAME = 'имя'
SECOND_NAME = 'отчество'
PHONE = 'телефон'
HEADERS = [ID, LAST_NAME, FIRST_NAME, SECOND_NAME, PHONE]


def load_directory(file_name = FILE_NAME):
    """Загружаю справочник вида list[dict[str, str]] из файла."""
    directory = []
    
    with open(file_name, 'r', encoding = 'utf-8') as file:
        """Оставим Альтернативный вариант из семинара"""
        for i, line in enumerate(file, start = 1):
            row = [i] + line.strip().split()
            directory.append(dict(zip(HEADERS, row)))

    return directory


def save_directory(directory: list[dict[str, str]], file_name=FILE_NAME):
    """Построчно сохраняю справочник в текстовый файл"""
    with open(file_name, 'w', encoding='utf-8') as file:
        for item in directory:
            file.write(' '.join(f'{value}' for key, value in item.items() if key != ID) + '\n')


def print_all_directory(directory):
    """Выводим на печать все записи справочника"""
    for item in directory:
        print(*(f"{k}: {v:<16}" for k, v in item.items()))


def add_contact(directory):
    """Добавляем новый контакт в справочник без сохранения в файл"""
    row = input('Введите Ф.И.О. и телефон, разделенные пробелами: ').split()
    line = [len(directory) + 1] + [item.strip().capitalize() for item in row]
    directory.append(dict(zip(HEADERS, line)))


def find_by_key(key: str, value: str, directory: list[dict[str, str]]):
    """Ищу совпадения значения в справочнике по столбцу key (ключ словаря)."""
    for item in directory:
        if item[key] == value:
            print(item)


def edit_by_id(number: str, directory):
    """Изменяю строку в справочнике без сохранения в файл"""
    if number.isdigit() and (id_ := int(number)) <= len(directory):
        print(*(f"{k}: {v:<16}"  for k, v in directory[id_ - 1].items()))
        row = input(
            'Введите исправленные ФИО и телефон, разделенные пробелами для замены: ').split()
        line = [id_] + [item.strip().capitalize() for item in row]
        directory[id_ - 1] = dict(zip(HEADERS, line))
        print('Данные обновлены')
    else:
        print(f'Такой {ID} отсутствует в справочнике. Возврат в меню...')


def delete_by_id(number: str, directory):
    """Удаляю строку в справочнике без сохранения в файл"""
    if number.isdigit() and (id_ := int(number)) <= len(directory):
        print(*(f"{k}: {v:<16}"  for k, v in directory[id_ - 1].items()))
        answer = input('Подтверждаете удаление (да/нет): ')
        if answer in {'y', 'yes', 'да'}:
            directory.pop(id_ - 1)
            print('Запись удалена')
    else:
        print(f'Такой {ID} отсутствует в справочнике. Возврат в меню...')


def edit_by_last_name(directory):
    """Запрашиваю фамилию и переименовываю всех однофамильцев"""
    old_value = input('Какую фамилию найти: ').strip().capitalize()
    new_value = input('На какую фамилию заменить: ').strip().capitalize()
    for item in directory:
        if item[LAST_NAME] == old_value:
            item[LAST_NAME] == new_value


def delete_by_first_name(directory):
    """Запрашиваю имя и удаляю по первому совпадению"""
    value = input('Какое имя удалить: ').strip().capitalize()
    for item in directory:
        if item in directory:
            directory.remove(item)
            break


def copy_line(number, directory):
    """Копируем строку нумбер в файл new_dir.txt"""
    if number.isdigit() and (id := int(number)) <= len(directory):
        print(*(f"{k}: {v:<16}" for k, v in directory[id - 1].items()))
        save_directory([directory[id - 1]], file_name='new_dir.txt')
    else:
        print(f'Такой {ID} отсутствует в справочнике. Возврат в меню...')


def main(directory):
    """Цикл событий с основным меню"""
    while True:
        print(f"""\nЧто хотите сделать?
        1: Вывести все данные
        2: Записать новый контакт
        3: Найти контакт по полю '{LAST_NAME}'
        4: Найти контакт по полю '{FIRST_NAME}'
        5: Изменить конктакт по полю '{ID}'
        6: Удалить конктакт по полю '{ID}'
        7: Изменить поле '{LAST_NAME}'
        8: Удалить по полю '{FIRST_NAME}'
        9: Скопировать строку по '{ID}' в новый файл
        0: Сохранить и выйти""")
        x = input()

        if x == '1':
            print_all_directory(directory)
        elif x == '2':
            add_contact(directory)
        elif x == '3':
            find_by_key(key=LAST_NAME,
                        value=input(
                            f'{LAST_NAME.title()}: ').strip().capitalize(),
                        directory=directory)
        elif x == '4':
            find_by_key(key=FIRST_NAME,
                        value=input(
                           f'{FIRST_NAME.title()}: ').strip().capitalize(),
                        directory=directory) 
        elif x == '5':
            edit_by_id(number=input(f'Введите {ID}, который хотите изменить: '),
                       directory=directory)
        elif x == '6':
            delete_by_id(number=input(f'Введите{ID}, который хотите удалить: '),
                         directory=directory)
        elif x == '7':
            edit_by_last_name(directory=directory)
        elif x == '8':
            delete_by_first_name(directory=directory)
        elif x == '9':
            copy_line(number=input(f'Введите {ID}, который хотите скопировать в отдельный файл: '),
                      directory=directory)
        elif x == '0':
            save_directory(directory)
            break
        else:
            print('Неверная команда!')    



if __name__ == "__main__":
    main(load_directory())