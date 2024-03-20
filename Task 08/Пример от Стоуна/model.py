phone_book = {}
path = 'Task 08\Пример от Стоуна\phone.txt'
SEPARATOR = ';'                                                      # Разделитель выводим в константу чтобы было проще изменять код

def open_phone_book():                                               # Открывает телефонную книгу из нашего файла со списком контактов.
    global phone_book
    with open(path, 'r', encoding='utf-8') as file:
        data = file.readlines()
    for u_id, contact in enumerate(data, 1):                         # Вводим переменную u_id и нумерацию чтобы проще было искать внутри программы (динамческие id)
        phone_book[u_id] = contact.strip().split(SEPARATOR)                             # .strip() помогает отчистить от переходовна новую строку
    
    
def save_phone_book():                                                  # Сохранение контакта
    global phone_book
    data = []
    for contact in phone_book.values():
        data.append(SEPARATOR.join(contact))
    data = '\n'.join(data)
    with open(path, 'w', encoding='utf-8') as file:
        file.write(data)


def _next_id():                                                         # Защищенная функция: когда есть "_" в начале имени функции, то та функция используется только в этом модуле
    global phone_book                                                   # не предназначена для других модулей, добавляет следующий id
    return max(phone_book) + 1 if phone_book else 1
    # if phone_book:
    #     return max(phone_book) + 1                                      # Функция "max" проходится по ключам
    # else:
    #     return 1
    
    
    
def add_new_contact(new_contact: list[str]):                            # Добавление нового контакта
    global phone_book
    phone_book[_next_id()] = new_contact
    
    
def find_contact(search_word: str) -> dict[int, list[str]]:             # Поиск контакта
    global phone_book
    result = {}
    for u_id, contact in phone_book.items():
        if search_word.lower() in ' '.join(contact).lower():                            # Чтобы искал через пробел
            result[u_id] = contact
    return result


def edit_contact(u_id: int, edited_contact: list[str]) -> str:                 # Изменение контакта
    '''
    Функция именения контакта в телефонной книге
    :param u_id: id пользователя в нашей телефонной книге
    :param edited_contact: Измененные данные пользователя
    :return: Имя измененного пользователя
    '''
    global phone_book
    current_contact = phone_book[u_id]
    for i in range(len(current_contact)):
        current_contact[i] = edited_contact[i] if edited_contact[i] else current_contact[i]
    phone_book[u_id] = current_contact
    return current_contact[0]

def delete_contact(u_id: int) -> str:
    global phone_book
    return phone_book.pop(u_id)[0]



# help(edit_contact)