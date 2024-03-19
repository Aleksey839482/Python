# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной.

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Алексей +79854563895 домашний
# Афанасий +78654956124 рабочий
# Марина +78659645711 рабочий
# Ирина +73422334566 рабочий
# Андрей +76654321177 домашний


# Должен уметь:
# 1 Показывать все контакты
# 2 Добавлять контакт
# 3 Найти контакт
# 4 Изменять контакт
# 5 Удалять контакт.

# Имя Номер Коммент                     encoding = 'utf-8'

my_dict = []

with open('phone.txt', 'r', encoding = 'utf-8') as file:
    for line in file:
        my_list = line.split()
        my_dict.append({'Имя':my_list[0], 'Телефон':my_list[1], 'Комменарий':my_list[2]})
        
# print(my_dict)

# print("""Выберете нужнуй пункт меню: 
#     1. Показывать все контакты
#     2. Добавлять контакт
#     3. Найти контакт
#     4. Изменять контакт
#     5. Удалять контакт
#     6. Выход из программы""")
# while True:
#     try:
#         menu_item = int(input())
#         break
#     except ValueError:
#         print("Вы ввели не верное значение. Введите пункт из меню.")
#         next

def show_all(my_dict):
    print("Телефонный справочник:")
    for i in my_dict:
        print(i)

# def add_new_contact(my_dict):
#     name = input("Ведите имя: \n").lower()
#     phone = input("Введите номер телефона: \n").lower()
#     comment = input("Введите комментарий: \n").lower()
#     new_string = f'\n{name} {phone} {comment}'
#     my_dict.append({'Имя':name, 'Телефон':phone, 'Комменарий':comment})
#     with open('phone.txt', 'a+', encoding = 'utf-8') as file:
#         file.write(new_string)

show_all(my_dict)
# add_new_contact(my_dict)
# show_all(my_dict)

def find_contact(my_dict):
    search_word = input("Ведите текст для поиска: \n")
    search_result = []
    for item in range(len(my_dict)):
        for i in my_dict[item].values():
            if search_word in i:
                print(my_dict[item])
                search_result.append(item)
    print(search_result)
    return search_result

find_contact(my_dict)

def chenge_contact(my_dict, index):
    fields = list(my_dict[0].keys())
    print(fields)
    temp_dict = my_dict[index]
    to_change = int(input("""Выберете что хотите изменить: 
1. Имя
2. Телефон
3. Комментарий \n\n"""))
    new_value = input("Введите новое значение: ")
    temp_dict[fields[to_change - 1]] = new_value
    my_dict = temp_dict
    with open('phone.txt', 'w', encoding = 'utf-8') as file:
        for i in my_dict:
            file.write(f'{i["Имя"]} {i["Телефон"]} {i["Комментарий"]}\n')

chenge_contact(my_dict, 1)
show_all(my_dict)
