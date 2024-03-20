import text


def show_main_menu() -> int:                                                            # Выводит главное меню
    for i, item in enumerate(text.main_menu):
        if i:
            print(f'\t{i}. {item}')
        else:
            print(item)
    while True:
        choice = input(text.choice_main_menu)
        if choice.isdigit() and 0 < int(choice) < len(text.main_menu):
            return int(choice)
        print(text.choice_main_menu_error)
        

def show_message(message: str):                                                         # Просто красивый разделитель
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')
    
    
def show_contacts(phone_book: dict[int, [str]], error_message: str):                     # Показывает контакты которые есть в нашем файле
    if phone_book:
        print('\n' + '=' * 70)
        for u_id, contact in phone_book.items():
            print(f'{u_id: >3}. {contact[0]: <20} {contact[1]: <20} {contact[2]: <20}')
        print('=' * 70 + '\n')
    else:
        # show_message(text.empty_phone_book_error)
        show_message(error_message)                                 # Чтобы не делать отдельно функцию для поиска, для показа контакта и для всего остального
        
        
def input_data(message) -> list[str] | str:                         # Добавление нового контакта или поиск
    if isinstance(message, str):
        return input('\n' + message)
    return [input(mes) for mes in message]

