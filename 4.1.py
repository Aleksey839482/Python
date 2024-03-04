# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию .split()

# Вариант с разрезами:

# my_str = input('Введите символычерез пробелы: ').split()              
# new_str = my_str[0] + " "

# for i in range(1 , len(my_str)):
#     if my_str[:i].count(my_str[i]):
#         new_str += f"{my_str[i]}_{my_str[:i].count(my_str[i])} "
#     else:
#         new_str += f"{my_str[i]} "
# print(new_str)


# Вариант со словарем:

my_str = input('Введите символычерез пробелы: ').split()
new_str = {}

for i in my_str:
    if i in new_str:
        print(f"{i}_{new_str[i]}", end = ' ')
    else:
        print(i, end = ' ')
    new_str[i] = new_str.get(i, 0) + 1